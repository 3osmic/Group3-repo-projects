_______________________________________________________________________

	Group 3	API Testing LAB	
_______________________________________________________________________


## LAB 04	API Automation with Python Requests Module

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


### Step 5: The GET Request (Postman Example)

### Step 6: The PUT Request (Postman Example)

### Step 7: The DELETE Request (Postman Example)

## FAQ (Frequently Asked Questions)
 <a id="faq"></a>
 
### When I Call APIs, Where Can I Find the Token?
Below shows you where you can find your API token:

![api-token](https://github.com/CbarNC/Group3-repo-projects/blob/API-Testing/api-token.gif?raw=true)

### How Do I Change the HTTP Methods?