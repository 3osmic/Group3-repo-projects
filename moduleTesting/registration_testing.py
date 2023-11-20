import datetime
import unittest
from app import signup


class RegistrationTesting(unittest.TestCase):

    def test_validate_signup(self):
        form = signup(
            email='new@test.test',
            password='example', confirm_password='example')
        self.assertTrue(form)

    def test_validate_password_match(self):
        pass

