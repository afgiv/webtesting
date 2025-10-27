Requirement Analysis

Project Name: Flask Login and Registration

Version: 1.0

Prepared by: Amadeo F. Genio IV

Date: October 20, 2025


1. Introduction


This document will serve as a detailed analysis of both functional and non-funtional requirements
for the project. It will be the foundation of the test design ensuring all required features of the
project are met and aligned with user expectations.


2. Functional Requirements


| Req_ID | Description                                                                              | Priority |
|--------|------------------------------------------------------------------------------------------|----------|
| FR-001 | The system must allow new users to register with their username, email, and password     | High     |
| FR-002 | The system must prevent duplicate registration of email and username                     | High     |
| FR-003 | The system should validate user inputs and prevent empty fields                          | High     |
| FR-004 | The system should automatically log in newly registered users                            | High     |
| FR-005 | The system should only allow registered users to log in                                  | High     |
| FR-006 | The system should flash messages in case of error                                        | Medium   |
| FR-007 | The system should welcome the user with the registered username                          | Medium   |
| FR-008 | The system must maintain log in session until logout                                     | Medium   |
| FR-009 | The system must clear the session if the user logs out                                   | High     |
| FR-010 | The systems navigation bar buttons should reflect depending on the users sessions status | Medium   |

3. Non-Functional Requirements


| Req_ID  | Category      | Description                                             |
|---------|---------------|---------------------------------------------------------|
| NFR-001 | Performance   | Response time should not exceed 2s under normal load    |
| NFR-002 | Usability     | Form error messages should be clear and readable        |
| NFR-003 | Security      | Password must not be stored in plain text               |
| NFR-004 | Compatability | Application must run on different browsers and devices  |
| NFR-005 | Reliability   | Application should run on stable condition continuously |
| NFR-006 | Scalability   | Application must handle at least 100 concurrent users   |


4. Assumptions and Dependencies


| Type       | Description                                                            |
|------------|------------------------------------------------------------------------|
| Dependency | Application is hosted through local server                             |
| Dependency | Browsers and tools (Postman & JMeter) are all installed and accessible |
| Dependency | Latest version of the application to be tested is deployed             |
| Dependency | API endpoints are deployed                                             |
| Assumption | UI features like buttons and forms are complete                        |
| Assumption | Database is already present                                            |
| Assumption | Login and Registration page is complete and accessible                 |


