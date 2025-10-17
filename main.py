from flask import Flask, request, render_template, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user



app = Flask(__name__)
app.config['SECRET_KEY'] = "thisISjustASecret"


login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()




@app.route('/')
def home():
    return render_template("index.html", page="home")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = db.session.execute(db.select(Users).where(Users.email == email))
        user = result.scalar()

        if not user:
            flash("Email does not exist, please try again", "danger")
            return redirect(url_for('login'))
        elif user.password != password:
            flash("Password Incorrect, please try again", "danger")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('welcome'))

    return render_template("login.html", page="login")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user_email = db.session.execute(db.select(Users).where(Users.email == email))
        existing_user = user_email.scalar()
        user_username = db.session.execute(db.select(Users).where(Users.username == username))
        existing_username = user_username.scalar()

        if existing_user:
            flash ("That email already exist, please enter a new email or login instead", "danger")
            return redirect(url_for('register'))
        elif existing_username:
            flash("Username already in use, please try another one", "danger")
            return redirect(url_for('register'))
        else:
            new_user = Users(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('welcome'))

    return render_template("register.html", page="register")

@app.route('/welcome/', methods=['GET'])
@login_required
def welcome():
    return render_template("welcome.html", page="welcome")

@app.route('/logout')
def logout():
    logout_user()
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5003)