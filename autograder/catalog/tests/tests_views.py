'''
Created by:	Chris Stannard
Description: This is the test file for the catalog views
Last edited by:	Eric Zair
Last edited on:	04/09/2019
'''

from django.test import TestCase
from django.urls import reverse
from catalog.models import Course
from catalog.views import *
from django.contrib.auth.models import User


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

class AssignmentDetailViewTest(TestCase):

	def test_template_with_assingment(self):
		Assignment.objects.create(name='Assignment1')
		response = self.client.get(reverse('assignment_detail', args=[1]))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'catalog/assignment_detail.html')

	def test_template_without_assingment(self):
		response = self.client.get(reverse('assignment_detail', args=[1]))
		self.assertEqual(response.status_code, 404)

	def test_display(self):
		Assignment.objects.create(name='Assignment1')
		response = self.client.get(reverse('assignment_detail', args=[1]))
		assignment = Assignment.objects.get(id=1)
		self.assertContains(response, assignment.name)
		self.assertContains(response, assignment.due_date)

class LogoutTemplateTests(TestCase):
	# create user for testing reasons.
	def setUp(self):
		self.credentials = {'username': 'testuser', 'password': 'secret'}
		self.user = User.objects.create_user('usertest', password='secret')
		self.client.force_login(self.user)

    # make sure logout page is accessable to a user.
	def test_logout_exists(self):
		response = self.client.get(reverse('accounts-logout'))
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'accounts/logout.html')
