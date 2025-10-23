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


Entry Criteria

    1. Application is deployed and accessible in local environment

    2. Database's schema and tables are initialzied

    3. Test cases and RTM are reviewed and approved


Exit Criteria

    1. All test cases and RTM are tested and filled

    2. All founded critical and severe bugs are fixed and retested

    3. Test summary report is completed and approved


6. Testing Environment

    - Operating system: Windows 11

    - Browser: Google Chrome (latest version)

    - Framework: Flask

    - Database: SQLite

    - IDE/Code Editor: VS Code

    - Testing Tools: Postman, JMeter, Excel, ScreenToGif


7. Test Deliverables

    1. Requirement Analysis Document

    2. Requirement Traceability Matrix (RTM)

    3. Test Plan

    4. Test Cases Document

    5. Test Summary Report

    6. Evidence of Test Results


8. Risks and Mitigation


| Risk_ID | Description                                                              | Type           | Mitigation                                                                                    |
|---------|--------------------------------------------------------------------------|----------------|-----------------------------------------------------------------------------------------------|
| R-001   | User credentials might not be stored in the database                     | Functional     | Verify DB records after registration; confirm API success.                                    |
| R-002   | Application might crash or slow down during performance test             | Non-Functional | Perform load testing using JMeter or Postman. Monitor resource usage and optimize DB queries. |
| R-003   | Invalid email format might be accepted during registration               | Functional     | Implement strict frontend and backend email validation.                                       |
| R-004   | Test Environment or browser might not be compatible with the application | Non-Functional | Perform cross-browser and device compatability testing.                                       |
| R-005   | Login/Register page might fail to load due to API issues                 | Non-Functional | Verify API endpoints using postman; check server status and connectivity. 

9. Roles and Responsibilities


| Role          | Name               | Responsibility                    |
|---------------|--------------------|-----------------------------------|
| Test Designer | Amadeo F. Genio IV | Prepare and review test cases     |
| Test Executor | Amadeo F. Genio IV | Execute all planned tests         |
| Bug Reporter  | Amadeo F. Genio IV | Log and track all identified bugs |

10. Schedule

| Document                       | Start Date       | End Date         |
|--------------------------------|------------------|------------------|
| Requirement Analysis           | October 20, 2025 | October 20, 2025 |
| Test Plan                      | Oct. 21, 2025    | October 23, 2025 |
| Test Cases                     | October 23, 2025 | October 24, 2025 |
| Test Execution & Bug Reporting |                  |                  |
| Test Summary Report            |                  |                  |

11. Approval


| Name               | Role        | Signature | Date |
|--------------------|-------------|-----------|------|
| Amadeo F. Genio IV | QA Engineer |           |      |