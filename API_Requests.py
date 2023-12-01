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


# Call the function to make the requests
post_request()
get_request()
put_request()
delete_request()
