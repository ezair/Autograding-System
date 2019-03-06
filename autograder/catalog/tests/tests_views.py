from django.test import TestCase
from django.urls import reverse
from catalog.views import *

from django.contrib.auth.models import User
from django.test import Client


class IndexViewTest(TestCase):
    """Test for index view"""
    def test_index_template(self):
        response = self.client.get(reverse('catalog-index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/index.html')

class LogInPassTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/catalog/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

class LogInFailTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user('username', email='None', password='None')
    def test_login(self):
        # send login data
        response = self.client.post('/catalog/', self.credentials, follow=True)
        # should be logged in now
        self.assertFalse(response.context['user'].is_active)

class RegistrationRedirectTest(TestCase):

    def test_the_redirect(self):
        response = self.client.get(reverse('catalog-index'))
        self.assertContains(response, '<a href="%s">here</a>' % reverse("accounts-student_registration"), html=True)
