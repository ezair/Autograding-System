'''
Created by:	Chris Stannard
File:	accounts/tests.py
Description: This is the test file for the accounts app
Last edited by:	Eric Zair
Last edited on:	03/21/2019
'''
from django.test import TestCase
from django.urls import reverse
from catalog.views import *


class TestStudentRegistration(TestCase):
    def test_correct_template(self):
        response = self.client.get(reverse('accounts-student_registration'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/student_registration.html')