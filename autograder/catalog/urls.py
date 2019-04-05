'''
Created by: Chris S
File: catalog/urls.py
Description: contains all url/path and logic in regards
			 to routing for the catalog application.
Last edited by: Eric Zair
Last edited on:	03/04/2019
'''
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


# Stick to the nameing conventions for the name= parameter.
# it is always 'app_name-html_file_name' and nothing else.
urlpatterns = [
	path('my', views.my_view, name="catalog-my"),
]