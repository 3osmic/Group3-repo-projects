import unittest
from flask import Flask
from app import app
import sqlite3
import init_db

class RegistrationTesting(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

        self.conn = sqlite3.connect('database.db')
        self.conn.row_factory = sqlite3.Row
        init_db(self.conn)

    def test_validate_signup(self):
        # Data for the signup form
        data = dict(
            username='test_user1',
            email='new@test.test',
            password='example',
            confirm_password='example'
        )

        # Submit the signup form
        response = self.app.post('/signup', data=data, follow_redirects=False)

        # Follow the redirect manually
        redirect_response = self.app.get(response.headers['Location'])

        # Assert that the user is present in the database
        user_in_database = self.get_user_from_database(data['username'])
        self.assertIsNotNone(user_in_database)
        self.assertEqual(user_in_database['username'], data['username'])

    def get_user_from_database(self, username):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        return user


if __name__ == '__main__':
    unittest.main()


