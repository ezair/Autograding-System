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
	path('register/', views.StudentRegistrationView.as_view(),
						name='accounts-student_registration'),
	path('login/', LoginView.as_view(template_name='catalog/index.html'),
												  name="accounts-index"),
]