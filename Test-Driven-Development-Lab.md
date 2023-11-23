_______________________________________________________________________

	Group 3	Test-Driven Development LAB	
_______________________________________________________________________


## LAB 03	UNIT TESTING WITH TEST-DRIVEN DEVELOPMENT

### OBJECTIVES
- Understand unit testing using Python.
- Create pytest functions
- Provide details on commands commonly used in Behave

### PREREQUISITES
- Must have basic knowledge of software testing
- Must have a basic level of knowledge of the python programming language

## BEFORE YOU GET STARTED
You will need the following in order for your tests to perform correctly

- Create a GitHub account
  - Clone the GitHub repository
- Install a code editor
- Install python
- Install pytest

Examples of code editors:
- VS Code
- Pycharm (Recommended)

For more information on Installations and GitHub: https://github.com/CbarNC/Group3-repo-projects/blob/Selenium/Selenium%20Lab.md

### OVERVIEW
Test Driven Development (TDD) is the process of using unit testing to write automated test functions before writing the actual code. To achieve this, TDD uses multiple libraries with different languages, but in the lab, we will be focusing on the pytest library with python. The information below is a step-by-step guide on how to help you get started.

### What is Unit Testing?
Unit Testing is the process of checking small pieces of code to deliver information early and often

### Three Phases of TDD
1. **Red**: Think about what you want to develop
2. **Green**: Think about how to make your tests pass
3. **Refactor**: Think about how to improve your existing implementation

### Step 1: Install Pytest
You can install pytest using Python's package manager, pip. Open your command prompt or terminal and run the following command:

`pip install pytest`

![Pytest](img.png)

Once installed, a "Successfully installed" message should be displayed.

- For more information on pytest, visit their website at: https://docs.pytest.org/en/7.1.x/contents.html

Note: If you find that you have problems installing behave on your computer, please navigate to the [FAQ](#faq) section of this document

###  Step 2 (RED STAGE)
The purpose of this phase is to write a test that informs the implementation of a feature.

Here is an example of the "in the red" stage:
![s1](https://github.com/CbarNC/Group3-repo-projects/blob/Test-Driven-Development---(TDD)/s1.gif?raw=true)

###  Step 3 (GREEN STAGE)
The purpose of this phase is to 

Here is an example of the "in the green" stage:
![s2]()

###  Step 4 (REFACTOR STAGE)
The purpose of this phase is to implement your code better or more efficiently.

Here is an example of the "in the green refactor" stage:
![s3]()

###  Step 5 (Writing a Test File For the Signup Page)
Here is a breakdown of the test_app.py file:

```python
import unittest
from app import app, get_db_connection, db


class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['SECRET_KEY'] = 'testingdb123'
        self.app_ctxt = self.app.app_context()
        self.app_ctxt.push()
        self.client = self.app.test_client()
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
            table_exists = cursor.fetchone() is not None

        if not table_exists:
            # Create the users table for testing
            db(create_table=True)

    def tearDown(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DROP TABLE IF EXISTS users')
            conn.commit()

        self.app_ctxt.pop()

    def test_signup_successful(self):
        form_data = {
            'username': b'test_user12345',
            'email': b'existing@test.test',  # Existing email in the database
            'password': b'example',
            'confirm-password': b'example',
        }
        
        response = self.client.post('/signup', data=form_data, follow_redirects=True)
        
        print(response.data)
        
        assert b"Cuisine Page" in response.data
        assert response.status_code == 200
        assert response.request.path == '/index'
        
    def test_validate_password_match(self):
        form_data = {
            'username': b'test_user12345',
            'email': b'existing@test.test',  # Existing email in the database
            'password': b'example',
            'confirm-password': b'exampl',
        }

        response = self.client.post('/signup', data=form_data, follow_redirects=True)

        print(response.data)

        assert b"Passwords do not match" in response.data
        assert response.status_code == 200
        assert response.request.path == '/signup'

if __name__ == '__main__':
    unittest.main()
```

- **Import Statements**
  - `unittest`: The Python unit testing framework
  - `app`, `get_db_connection`, `db`: Parts of the web application being tested
- **TestRegistration() Class**
  -  Inherits from `unittest.TestCase`
- **Methods**
  - *setUp*
    - Configures the Flask app for testing, creates a test client, and checks if the 'users' table exists in the database
      - If not, it creates the table
  - *tearDown*
    - Drops the `users` table from the database
  - *test_signup_successful*
    - Sends a POST request to the '/signup' endpoint with some form data, simulating a user registration attempt
    - Checks if the response contains the expected content and has the expected status code and path
  - *test_validate_password_match*
    - Defines a test case for validating password match during signup
- *if __name__ == '__main__':*
  - Ensures that if the script is run directly (not imported as a module), the tests are executed

## FAQ (Frequently Asked Questions)
 <a id="faq"></a>
