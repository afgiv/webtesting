# Import necessary packages for the project
from flask import Flask, request, render_template, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required


# Create the Flask app instance
app = Flask(__name__)
# The secret key is used for session management, you can use whatevery key you want
app.config['SECRET_KEY'] = "thisISjustASecret"


# Create the base model
class Base(DeclarativeBase):
    pass
# Define the database to be stored locally and initialize the database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Define the Users table which will hold the details of each user
class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    # Originally, email will have a constraint of unique but we will create an intentional bug
    # This will be a duplicate email bug
    email: Mapped[str] = mapped_column(String(250), nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)


# Connect login manager to flask which helps login sessions automatically
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

# Create the database
with app.app_context():
    db.create_all()


# Renders the home page
@app.route('/')
def home():
    return render_template("index.html", page="home")


# Renders the log in page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the form in the log in page is submitted
    if request.method == 'POST':
        # Get the data from the form
        email = request.form['email']
        password = request.form['password']
        # Check if the user already exists in the database
        result = db.session.execute(db.select(Users).where(Users.email == email))
        user = result.scalar()
        # This will handle errors if credentials are not met
        if not user:
            flash("Email does not exist, please try again", "danger")
            return redirect(url_for('login'))
        elif user.password != password:
            flash("Password Incorrect, please try again", "danger")
            return redirect(url_for('login'))
        elif not email or not password:
            flash("Please fill out all fields")
            return redirect(url_for('login'))
        else:
        # If successful, automatically log in the user to the welcome page
            login_user(user)
            return redirect(url_for('welcome'))

    return render_template("login.html", page="login")

# Renders the register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    # If the form in the register page is submitted
    if request.method == 'POST':
        # Get all data from the form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Check if the user already exists in the database
        user_email = db.session.execute(db.select(Users).where(Users.email == email))
        existing_user = user_email.scalar()
        user_username = db.session.execute(db.select(Users).where(Users.username == username))
        existing_username = user_username.scalar()
        # This will handle all errors if credentials are not met
        # This will be an intentional bug - Duplicate emails
        # if existing_user:
        #     flash ("That email already exist, please enter a new email or login instead", "danger")
        #     return redirect(url_for('register'))
        if existing_username:
            flash("Username already in use, please try another one", "danger")
            return redirect(url_for('register'))
        elif not username or not email or not password:
            flash("Please fill out all fields")
            return redirect(url_for('register'))
        else:
        # If successful, add the data of the user to the database and automatically log in to the welcome page
            new_user = Users(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('welcome'))

    return render_template("register.html", page="register")


# Renders the welcome page, log in required is used as this will be the criteria to show that this page is for authenticated users only
@app.route('/welcome/', methods=['GET'])
@login_required
def welcome():
    return render_template("welcome.html", page="welcome")

# Renders the home page after a successful logout
@app.route('/logout')
def logout():
    logout_user()
    return render_template("index.html")


# Start the Flask app
if __name__ == "__main__":
    # Run the app in debug mode for development
    # app.run(debug=True, port=5003)

    app.run()