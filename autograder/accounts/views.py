'''
Created by:	Eric Zair
File:	accounts/views.py
Description:	Contains ALL views for our account application.
				Examples of these views:
					login view
					registration view
					etc...
Last edited by:	Eric Zair
Last edited on:	03/05/2019
'''
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms


# Create a view that will be used for User Registration.
# We base this view off of the django built in UserCreationForm
# Note, we will redirect users to the homepage, if form is successfully
# submitted.
class StudentRegistrationView(CreateView):
	form_class = forms.StudentRegistrationForm
	template_name = 'accounts/student_registration.html'
	success_url = reverse_lazy("catalog-index")