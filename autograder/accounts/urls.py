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
from .views import *


# All /accounts application pages here.
# Make sure to add the name = param, or everything will just suck.
urlpatterns = [
	path('register/', StudentRegistrationView.as_view(),
				  	name='accounts-student_registration'),
	]