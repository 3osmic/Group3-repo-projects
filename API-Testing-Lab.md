_______________________________________________________________________

	Group 3	API Testing LAB	
_______________________________________________________________________


## LAB 04	API Automation with Postman and Python Requests Module

### OBJECTIVES
- Understand unit testing using Python.
- Create pytest functions
- Provide details on commands commonly used in Behave

### PREREQUISITES
- Must have basic knowledge of software testing
- Must have a basic level of knowledge of the python programming language
- Must have basic knowledge of APIs

## BEFORE YOU GET STARTED
You will need the following in order for your tests to perform correctly

- Install a web browser to run the web application
    - This can be:
        - Firefox (Recommended)
        - Chrome
        - Microsoft Edge
- Create a GitHub account
  - Clone the GitHub repository
- Install a code editor
- Create a Postman account
- Download Postman desktop
- Install the python `requests` library

Examples of code editors:
- VS Code
- Pycharm (Recommended)

For more information on Installations and GitHub: https://github.com/CbarNC/Group3-repo-projects/blob/Selenium/Selenium%20Lab.md

### OVERVIEW
API testing refers to the process of testing the application programming interfaces (APIs) of a software system. In this lab, you'll harness the simplicity of Postman for manual testing and leverage the versatility of the Python `requests` library for automated scenarios. The information below is a step-by-step guide on how to help you get started.

### What Are APIs?
APIs are sets of rules and protocols that allow different software applications to communicate with each other.

### Step 1: Create a Postman Account
To create a Postman account, first navigate to this website: https://www.postman.com

You can either create an account manually, through Google, or SSO.

![postman-create-account](https://github.com/CbarNC/Group3-repo-projects/blob/API-Testing/postman-create-account.gif?raw=true)

### Step 2: Install the `requests` Python Library
You can install the `requests` library by using the following command in either the command line or terminal:

`pip install requests`

![pip-install-requests](https://github.com/CbarNC/Group3-repo-projects/blob/API-Testing/pip-install-requests.gif?raw=true)

### Step 3: Retrieve the Local Host Link
In order to retrieve the local host link to test the APIs, open up your terminal in your code editor. In this example, I am using python's terminal:

- Run the app.py file for flask:

![local-host-link](https://github.com/CbarNC/Group3-repo-projects/blob/API-Testing/local-host-link-new.gif?raw=true)

### Step 4: The POST Request (Postman Example)
We will first begin this lab by demonstrating how to test APIs in Postman. 

Steps:
1. Run your flask file
2. Take the link we copied earlier for the signup page and paste it in the `POST` HTTP method url area
3. Click "Body" in one of the columns below
4. You should see a dropdown for the `form-data` - select it
5. Fill in the info for the sign-up as you usually would (username, email, password, and confirm password)
6. Click `Send`
7. You should see a `200` request

- If you want to check if the user was successfully created, you can by going into your code editor and selecting the `database.db` file
- Refresh the table and you should see your newly created user!

Example:

https://github.com/CbarNC/Group3-repo-projects/assets/137305186/de252628-89d0-4e1a-a7cf-791a26e9ede0




### Step 5: The GET Request (Postman Example)
In order for you to fetch the user currently in the database, I included a new html file that holds all the user info:

`admin_dashboard.html`

Steps:
1. Copy the local host website
2. Paste the link in the `GET` HTTP method url area
3. Add `/admin/dashboard` to the end of the url
4. Click `Send`
5. You should see a `200` request
6. Click `Preview` in the columns below

Example:


https://github.com/CbarNC/Group3-repo-projects/assets/137305186/37e5e27d-2cb1-4e78-b779-9d9ce52e71d2



### Step 6: The PUT Request (Postman Example)
In order for you to update the user currently in the database, I included this html file that holds the user info:

`admin_dashboard.html`

Steps:
1. Copy the local host website
2. Paste the link in the `PUT` HTTP method url area
3. Add `/update_user/(username)` to the end of the url
4. Change the `form-data` `username`/`email` to `new_username`/`new_email`
5. Change the name and email to the ones you want to update
6. Click `Send`
7. You should see a `200` request
8. Click `Preview` in the columns below to see the new updated input boxes
9. Go back to your code editor and refresh the database to see your updated username and email info

Example:


https://github.com/CbarNC/Group3-repo-projects/assets/137305186/5ae095c8-b255-42db-9dfc-2a2d2815f308



### Step 7: The DELETE Request (Postman Example)
In order for you to delete the user currently in the database, I included this html file that holds the user info:

`admin_dashboard.html`

Steps:
1. Copy the local host website
2. Paste the link in the `DELETE` HTTP method url area
3. Add `/delete_user/(username)` to the end of the url
4. Click `Send`
5. You should see a `200` request
6. Click `Preview` in the columns below to see a blank page (without any users)
7. Go back to your code editor and refresh the database to see your user has been deleted

Example:


https://github.com/CbarNC/Group3-repo-projects/assets/137305186/68f66136-4e93-467a-bfa4-2c30a07346ba



## FAQ (Frequently Asked Questions)
 <a id="faq"></a>

### What Do The Different HTTP Methods Mean?

### How Do I Change the HTTP Methods?

### My Database Is Not Showing My User Data