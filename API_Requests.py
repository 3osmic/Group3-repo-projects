
"""
import requests

# base url (signup):
signup_url = 'http://127.0.0.1:5000/signup'


def post_request():
    signup_data = {
        'username': b'test_user12345',
        'email': b'existing@test.test',
        'password': b'example',
        'confirm-password': b'example',
    }

    response = requests.post(signup_url, data=signup_data)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print(".....USER CREATED.....")
        print("=======================")

        # After successful signup, make a GET request to retrieve user information
        get_user_info()
    else:
        print('Signup failed. Status code:', response.status_code)
        print('Response content:', response.text)


def get_user_info():
    # Make a GET request to retrieve user information
    response = requests.get('http://127.0.0.1:5000/signup')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print('User Information:')
        print(response.json())
    else:
        print('Failed to get user information. Status code:', response.status_code)
        print('Response content:', response.text)


# Call the function to make the POST request
post_request()

"""