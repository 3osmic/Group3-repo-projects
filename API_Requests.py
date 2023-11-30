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
        print('Signup successful!')
    else:
        print('Signup failed. Status code:', response.status_code)
        print('Response content:', response.text)


post_request()

def get_request():
    pass

"""
# POST (Create User)
def post_request():
    print("post url:" + base_url)

    data = {
        'username': 'test_user12345',
        'email': 'create@test.test',
        'password': 'example',
        'confirm-password': 'example',
    }

    response = requests.post(base_url, data=data)  # Use data instead of json
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body: ", json_str)
    username = json_data["username"]
    assert "email" in json_data
    assert json_data["email"] == "test_user12345"
    print(".....POST USER IS DONE....")
    print(".....======================.....")
    return username


# GET (Get User)
def get_request():
    print("get url:" + base_url)
    response = requests.get(base_url)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body: ", json_str)
    print(".....GET USER IS DONE....")
    print(".....======================.....")


# PUT (Update User)
def put_request(username):
    url = base_url + f"/{username}"
    print("put url: " + url)
    data = {
        'username': 'test_user12345',
        'email': 'update@test.test',
        'password': 'example',
        'confirm-password': 'example',
    }

    response = requests.put(url, json=data)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response body: ", json_str)
    assert json_data["username"] == username
    assert json_data["email"] == "update@test.test"
    print("....PUT USER IS DONE....")
    print(".....======================.....")


# DELETE (Delete User)
def delete_request(username):
    url = base_url + f"/{username}"
    print("DELETE url: " + url)
    response = requests.delete(url)
    assert response.status_code == 204
    print(".....DELETE USER IS DONE....")
    print(".....======================.....")


# call
get_request()
username = post_request()
put_request(username)
delete_request(username)

"""
