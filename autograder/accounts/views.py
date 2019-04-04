'''
Created by:	Eric Zair
File:	accounts/views.py
Description:	Contains ALL views for our account application.
				Examples of these views:
					login view
					registration view
					etc...
Last edited by:	Eric Zair
Last edited on:	04/04/2019
'''
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from . import forms
from django.shortcuts import render



# View for an admin, when registering a user to the database.
# The user currently has no group associated with it, however,
# this is something that we will add.
def register_account_view(request):
	form = forms.UserRegistrationForm(request.POST or None)
	# Grab the information from the user and make sure that the
	# email field has been filled out successfully.
	if request.POST and form.is_valid():
		# We now parse the email field given on the form, which allows us
		# to create the account username.
		username = form.cleaned_data['email'].split('@')[0]
		# The password needs to be a random gened one, so that
		# only the user is aware of what it may be.
		password = 'testpassword'
		user = User.objects.create_user(username=username,
										password=password,
										email=form.cleaned_data['email'])
		user.save()
		# This is where we will have to send the "invite" email to the user.
		return render(request, 'accounts/registration.html', {'form' : form})
	return render(request, 'accounts/registration.html', {'form' : form})