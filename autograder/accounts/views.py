'''
Created by:	Eric Zair
File:	accounts/views.py
Description:	Contains ALL views for our account application.
				Examples of these views:
					login view
					registration view
					etc...
Last edited by:	Eric Zair
Last edited on:	02/27/2019
'''
from django.contrib.auth import authenticate, login
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create a view that will be used for User Registration.
# We base this view off of the django built in UserCreationForm
# Note, we will redirect users after form is validated and successful.
class StudentRegistrationView(CreateView):
	form_class = CustomUserCreationForm
	# Currently url is sending to home page.
	# it may not work, but we don't care right now.
	successful_url = reverse_lazy("/")
	template_name = 'accounts/student_registration.html'