import requests
import json
import random
import string


#base url (signup):
base_url = http://127.0.0.1:5000/signup

# POST (Create User)
def post_request():
    print("post url:" + base_url)

    data = {
        'username': 'test_user12345',
        'email': 'create@test.test',
        'password': 'example',
        'confirm-password': 'example',
    }

    request.post(base_url, json=data)
    assert response.status_code == 201
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body: ", json_str)
    username = json_data["username"]
    assert "email" in json_data
    assert json_data["email"] == "test_user12345"
    return username
    print(".....POST USER IS DONE....")
    print(".....======================.....")

# GET (Get User)
def get_request():
    print("post url:" + base_url)
    reponse = requests.get(base_url)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json response body: ", json_str)
    print(".....GET USER IS DONE....")
    print(".....======================.....")

# PUT (Update User)
def put_request():
    print("post url: " + base_url)
    data = {
        'username': 'test_user12345',
        'email': 'update@test.test',
        'password': 'example',
        'confirm-password': 'example',
    }

    reponse = requests.put(base_url, json=data)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json PUT response body: ", json_str)
    assert json_data["username"] == username
    assert jason_data["email"] == "update@test.test"
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

#call
get_request()
username = post_request()
put_request(username)
delete_requests(username)