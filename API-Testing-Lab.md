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
3. Add `/get_user/(username)` to the end of the url
4. Click `Send`
5. You should see a `200` request
6. When looking below in the `Body` section of the `Pretty` tab, you should see your user info in a json format

Example:


https://github.com/CbarNC/Group3-repo-projects/assets/137305186/21a24663-97c0-4a90-be04-badc80903dad




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



### Step 8: The POST Request (Requests Library Example)
Below is a breakdown of the code shown in the example:

**Example:**


**BREAKDOWN:**
```python
import requests

# base url (signup):
signup_url = 'http://127.0.0.1:5000'


# POST Request
def post_request():
    create_signup = signup_url + '/signup'

    signup_data = {
        'username': 'test_user',
        'email': 'test@email.com',
        'password': 'example',
        'confirm-password': 'example',
    }

    response = requests.post(create_signup, data=signup_data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(".....USER CREATED.....")
        print("=======================\n")

    else:
        print('Signup failed. Status code:', response.status_code)
        print('Response content:', response.text)


post_request()
```


### Step 9: The GET Request (Requests Library Example)
Below is a breakdown of the code shown in the example:

**Example:**


**BREAKDOWN:**
```python
import requests

# base url (signup):
signup_url = 'http://127.0.0.1:5000'


# GET Request
def get_request():
    get_user_info = signup_url + '/get_user/test_user'

    # Make a GET request to retrieve user information
    response = requests.get(get_user_info)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(".....GET REQUEST CREATED.....")
        print("=============================")
        print('User Information:')
        print(response.json())
        print("\n")
    else:
        print('Failed to get user information. Status code:', response.status_code)
        print('Response content:', response.text)


get_request()
```

### Step 10: The PUT Request (Requests Library Example)
Below is a breakdown of the code shown in the example:

**Example:**


**BREAKDOWN:**
```python
import requests

# base url (signup):
signup_url = 'http://127.0.0.1:5000'


# PUT Request
def put_request():
    put_updated_info = signup_url + '/update_user/test_user'

    updated_data = {
        'new_username': 'test_user_updated',
        'new_email': 'testupdated@email.com',
    }

    response = requests.put(put_updated_info, data=updated_data)

    if response.status_code == 200:
        print(".....PUT REQUEST CREATED.....")
        print("=============================")
        print('User Information:')

        get_user_info = signup_url + '/get_user/test_user_updated'

        # Make a GET request to retrieve user information
        response_updated = requests.get(get_user_info)

        # After successful signup, make a response request to retrieve user information
        print(response_updated.json())
        print("\n")
    else:
        print('Failed to update user information. Status code:', response.status_code)
        print('Response content:', response.text)


put_request()
```
### Step 11: The DELETE Request (Requests Library Example)
Below is a breakdown of the code shown in the example:

**Example:**


**BREAKDOWN:**
```python
import requests

# base url (signup):
signup_url = 'http://127.0.0.1:5000'


# DELETE Request
def delete_request():
    delete_info = signup_url + '/delete_user/test_user_updated'

    response = requests.delete(delete_info)

    if response.status_code == 200:
        print(".....DELETE REQUEST CREATED.....")
        print("================================\n")

    else:
        print('Failed to delete user information. Status code:', response.status_code)
        print('Response content:', response.text)


delete_request()

```
## FAQ (Frequently Asked Questions)
 <a id="faq"></a>

### What Do The Different HTTP Methods Mean?

1. **POST**
   - Create a user
2. **GET**
   - Retrieve user or users
3. **PUT**
   - Update user data
4. **DELETE**
   - Delete a user

### How Do I Change the HTTP Methods in Postman?
To change the HTTP methods, you can click the dropdown menu:


https://github.com/CbarNC/Group3-repo-projects/assets/137305186/efb0525d-d7e3-4a6f-a37b-7433eb8f0d1c



### My Database Is Not Showing My User Data
Your SQL database may not be showing because you have not installed the SQL extension

Example:


https://github.com/CbarNC/Group3-repo-projects/assets/137305186/38a99f43-6ec1-410c-9410-0136f2038aa1

