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


    def test_user_name_valid(self):



if __name__ == '__main__':
    unittest.main()
