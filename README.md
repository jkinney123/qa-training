# QA Training Project Readme
This project uses the Replit IDE, which is located https://replit.com/@aungminedu/qa-training#README.md

The technologies involved with this project are [Python](https://www.python.org/), [SQLite w/Python](https://www.geeksforgreeks.org/python-sqlite/),[Selenium](https://www.selenium.dev/).

The skills developed in this project are:
1. Git & Github
2. Writing Python Code
3. Writing SQL
4. Implementing Selenium
5. Learning core QA Concepts & Methodologies


SauceDemo QA Testing: 

User Story 1: 
As a standard user, I want to log in to the application successfully so that I can access the inventory and browse products for purchase.

Test Case 1-
Objective: Verify that standard_user can log in successfully.

Steps:
1. Navigate to saucedemo.com.
2. Enter username standard_user.
3. Enter password secret_sauce.
4. Click "Login".
5. Verify that the inventory page loads.

Expected Result: The user is logged in, and the inventory page is displayed promptly.

Script to run - ./saucedemo/standard_user_login.py


User Story 2:
As a user experiencing performance issues, I want to log in to the application without significant delays so that I can access the inventory and use the app efficiently.

Test Case 2- 
Objective: Verify that the login process performs smoothly and does not cause unnecessary delays for the user.

Steps:
1. Measure the login time for standard_user (baseline performance).
2. Measure the login time for performance_glitch_user.
3. Compare the login times to identify any significant delays.

Expected Result: The login time for performance_glitch_user should be within an acceptable range compared to the baseline. Any significant delay indicates a performance issue that needs to be addressed.

Script to run - ./saucedemo/performance_comparison.py
