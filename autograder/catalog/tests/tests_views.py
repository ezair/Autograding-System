'''
Created by:	Chris Stannard
Description: This is the test file for the catalog views
Last edited by:	Chris Stannard
Last edited on:	03/06/2019
'''

from django.test import TestCase
from django.urls import reverse
from catalog.views import *

from django.contrib.auth.models import User
from django.test import Client


class IndexTemplateTest(TestCase):
    """Test for index view"""
    def test_index_template(self):
        response = self.client.get(reverse('catalog-index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/index.html')

class IndexLogInPassTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        # create user using credentials
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/catalog/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

class IndexLogInFailTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        # create user using different credentials
        User.objects.create_user('usertest', password='secret')
    def test_login(self):
        # send login data
        response = self.client.post('/catalog/', self.credentials, follow=True)
        # should not be logged in now
        self.assertFalse(response.context['user'].is_active)
        # a message should be viewable
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')

class IndexRedirectToRegistrationTest(TestCase):
    def test_the_redirect(self):
        response = self.client.get(reverse('catalog-index'))
        # checks to see if the link is there and gets the correct template
        self.assertContains(response, '<a href="%s">here</a>' % reverse("accounts-student_registration"), html=True)
