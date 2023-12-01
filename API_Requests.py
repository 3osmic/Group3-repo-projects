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
        print("=======================")

        # After successful signup, make a GET request to retrieve user information
        get_request()
    else:
        print('Signup failed. Status code:', response.status_code)
        print('Response content:', response.text)


# GET Request
def get_request():
    # Make a GET request to retrieve user information
    response = requests.get('http://127.0.0.1:5000/signup')

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        print('User Information:')
        print(response.json())
    else:
        print('Failed to get user information. Status code:', response.status_code)
        print('Response content:', response.text)


# PUT Request


# DELETE Request


# Call the function to make the requests
post_request()
get_request()