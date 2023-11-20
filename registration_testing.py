import unittest
from flask import Flask
from app import app

class RegistrationTesting(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_validate_signup(self):
        response = self.app.post('/signup', data=dict(
            username='test_user12345',
            email='new@test.test',
            password='example',
            confirm_password='example',
        ), follow_redirects=True)
        
        print(response.data)
        self.assertIn(b'Cuisine Page', response.data)

    def test_validate_password_match(self):
        pass
    
if __name__ == '__main__':
    unittest.main()