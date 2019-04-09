'''
Created by:	Chris Stannard
Description: This is the test file for the catalog views
Last edited by:	Eric Zair
Last edited on:	04/08/2019
'''

from django.test import TestCase
from django.urls import reverse
from catalog.models import Course
from catalog.views import *
from django.contrib.auth.models import User
from django.test import Client


class CatalogTemplateTests(TestCase):
	"""Test for index view"""
	def test_index_template(self):
		response = self.client.get(reverse('catalog-my'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'catalog/my.html')

	# create user for testing reasons.
	def setUp(self):
		self.credentials = {'username': 'testuser', 'password': 'secret'}
		self.user = User.objects.create_user('usertest', password='secret')
		self.client.force_login(self.user)


class IndexLogInPassTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        # create user using credentials
        User.objects.create_user(**self.credentials)
    
    def test_login(self):
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
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
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should not be logged in now
        self.assertFalse(response.context['user'].is_active)
        # a message should be viewable
        self.assertContains(response, 'Please enter a correct username and password. Note that both fields may be case-sensitive.')


# class IndexRedirectToRegistrationTest(TestCase):
#     def test_the_redirect(self):
#         response = self.client.get(reverse('catalog-my'))
#         # checks to see if the link is there and gets the correct template
#         self.assertContains(response, '<a href="%s">here</a>' % reverse("accounts-registration"), html=True)