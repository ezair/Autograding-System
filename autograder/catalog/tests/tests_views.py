from django.test import TestCase
from django.urls import reverse
from catalog.views import *

class TestIndexViews(TestCase):
    """Test for index view"""
    def test_index_template(self):
        response = self.client.get(reverse('catalog-index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/index.html')

    def test_login(self):
        response = self.client.get(reverse('catalog-index'))
        self.assertEqual(response.status_code, 200)
        post_response = self.client.post(reverse('catalog-index'),
            data={'exampleInputEmail1': "test@example.com",
                  'password1': "icantthinkofanything"})
        self.assertEqual(post_response.status_code, 302)
        user = CustomUser.objects.get(id=1)
        #user = User.objects.get(id=1)
        self.assertEqual(user.email, 'test@example.com')
