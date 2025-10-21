Test Plan ID: TP-001
Project Name: Flask Web Login and Registration
Version: 1.0
Prepared By: Amadeo F. Genio IV
Date: October 19, 2025

1. Introduction

This test plan defines the testing strategy, scopes, approach, and deliverables of the project,
Flask Web Login and Registration web application. The purpose of this testing is to ensure that the
flow of the web app work as intended -- user registration and login functionalities, handling invalid
inputs or duplicate accounts, user feedbacks during these errors, and UI functionalities such as buttons.

2. Objective

The objective of this test effort is to validate the reliability, usability, and correctness of the login
and registration workflow. The goal is to ensure that:
    - New users can successfully register using valid credentials
    - Existing users can login with the correct credentials
    - Duplicate Email registration and Username is prevented
    - Navigation elements dynamically adjust based on the users session state

3. Scope

The scope of the test will test all features existing in the current release/version:

In Scope:
    1. User registration
        - Form validation for username, email, and password
        - Prevention of duplicate email and username
        - Automatic login after successful registration
    2. User Login
        - Verifcation of correct/incorrect credentials
        - Flash message display for unsuccessfull entries
        - Welcome page to corresponding user's username upon successfull login
    3. User Session Management
        - Session persistent after login
        - Logout functionality and redirection to home page
        - Verification of welcome page only for logged in users
    4. UI Functionality
        - Correct buttons for each page depending on the users session status
    5. Database Integrity
        - Verify each users credentials are added to the database

Out of Scope:
    1. Forgot Password (Not yet implemented)
    2. Password hash security (Not yet implemented)
    3. Login ban after consectutive unsuccessfull tries (Not yet implemented)

4. Testing Approach

The testing approach for this project will primarily focus on Black Box Testing Appraoch
to validate the flow of the user-features such as registration, login, logout, and navigation.
The testers will perform both manual and automated validation to make sure the system acts accordingly
to its purpose.

Additionaly, Non-Functional testing methods will be added to ensure the system will perform well like
system responsiveness, user experience, security, and performance.

5. Entry and Exit Criteria


