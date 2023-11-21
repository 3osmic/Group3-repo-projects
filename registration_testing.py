import unittest

import pytest

from app import app
import os

os.environ['DATABASE_URL'] = 'sqlite://'


class RegistrationTesting(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.app.config['SECRET_KEY'] = 'testingdb123'
        self.app_ctxt = self.app.app_context()
        self.app_ctxt.push()
        # db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        # db.drop_all()
        self.app_ctxt.pop()
        self.app = None
        self.app_ctxt = None
        self.client = None

    def test_validate_signup(self):
        self.app.post('/signup', data=dict(
            username='test_user12345',
            email='new@test.test',
            password='example',
            confirm_password='example',
        ), follow_redirects=True)

        self.client.get('/index', follow_redirects=True)

        # assert b"Cuisine Page" in response.data
        # assert response.status_code == 200
        # assert response.request.path == '/index'
        # print(response.data)
        # self.assertIn(b'Cuisine Page, response.data')

    def test_validate_password_match(self):
        response = self.client.post('/signup', data={
            'username': 'group3',
            'password': '12345',
            'confirm_password': '1234'
        })
        # assert response.status_code == 200
        # html = response.get_data(as_text=True)
        # assert "Field must be equal to password." in html


if __name__ == '__main__':
    unittest.main()
