'''
Created by:	Chris Stannard
File:	accounts/tests.py
Description: This is the test file for the accounts app
Last edited by:	Eric Zair
Last edited on:	04/08/2019
'''
from django.test import TestCase
from django.urls import reverse
from catalog.views import *


# Admin should be able to access registration page.
class TestRegistration(TestCase):
	# create user for testing reasons.
	def setUp(self):
		self.credentials = {'username': 'testuser', 'password': 'secret'}
		self.user = User.objects.create_superuser(username='usertest',
												  password='secret',
												  email="testemail@gmail.com")
		self.client.force_login(self.user)
	
	def test_correct_template(self):
		response = self.client.get(reverse('accounts-registration'))
		self.assertEqual(response.status_code, 200)	
		self.assertTemplateUsed(response, 'accounts/registration.html')


# Test to see if a regular user can access registration page.
# NOTE: THEY SHOULD NOTE.
class TestFailedRegistration(TestCase):
	# create user for testing reasons.
	def setUp(self):
		self.credentials = {'username': 'testuser', 'password': 'secret'}
		self.user = User.objects.create_user(username='usertest', password='secret')
		self.client.force_login(self.user)
	
	# def test_incorrect_template(self):
	# 	response = self.client.get(reverse('accounts-registration'))
	# 	self.assertEqual(response, 404)
	# 	self.assertTemplateUsed(response.status_code, 'accounts/registration.html')