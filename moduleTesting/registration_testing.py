import datetime
import unittest
from unittest import TestCase

import app


class RegistrationTesting(TestCase):

    def test_validate_signup(self):
        form = signUp(
            email='new@test.test',
            password='example', confirm_password='example')
        self.assertTrue(form)

    def test_validate_password_match(self):


