'''
Created by:	Chris Stannard
Description: This is the test file for the catalog views
Last edited by:	Chris Stannard
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
		response = self.client.get(reverse('catalog-index'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'catalog/index.html')

	# create user for testing reasons.
	def setUp(self):
		self.credentials = {'username': 'testuser', 'password': 'secret'}
		User.objects.create_user('usertest', password='secret')
'''
	def test_my_template(self):
		client = Client()
		login = client.login(username='testuser', password='secret')
		# self.assertTrue(login)
		response = self.client.get(reverse('catalog-my'))
		self.assertEqual(response.status_code, 302)
		self.assertTemplateUsed(response, 'catalog/my.html')
'''

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

class CourseListViewTest(TestCase):

	# checks to see if the right template is used
	def test_template(self):
		response = self.client.get(reverse('courses'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'catalog/course_list.html')

	# checks to see if the response is there whithout courses
	def test_no_courses(self):
		response = self.client.get(reverse('courses'))
		self.assertContains(response, 'You have no courses.')

	# checks to see if there is a link with the courses name
	def test_with_courses(self):
		# create the course
		Course.objects.create(name='TestCoures')
		# get the course
		course = Course.objects.get(id=1)
		# get the page
		response = self.client.get(reverse('courses'))
		# checks to see if the page has a link with the courses name
		self.assertContains(response, course.name, html=True)
