'''
Created by:	Eric Zair
File: accounts/urls.py
Description:	Contains and manages the paths to all of our pages in
				the accounts/ application.
				This will include things like logins, logouts, student registrations,
				...etc
Last edited by:	Eric Zair
Last edited on:	02/27/2019
'''
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views


# Linking of all /accounts application pages here.
# Make sure to add the name = param, or everything will just suck.
urlpatterns = [
	path('register/', views.register_account_view, name='accounts-registration'),
	path('login/', LoginView.as_view(template_name='accounts/login.html'), name='accounts-login'),
	path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='accounts-logout'),
]