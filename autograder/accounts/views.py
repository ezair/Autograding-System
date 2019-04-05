'''
Created by:	Eric Zair
File:	accounts/views.py
Description:	Contains ALL views for our account application.
				ALL VIEWS WILL HAVE THE WORD "view" at the end of them.
				If not, then it is simply a helper method.
				Examples of these views:
					login view
					registration view
					etc...
				There will also be methods that are used for specific things
				such as sending emails.
Last edited by:	Eric Zair
Last edited on:	04/04/2019
'''
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import Http404
from . import forms


# Created to make sure that pages that should only be accessed by
# admins...are only accessed by admins.
# If a regular user attempts to access them, we give them page not found.
def error_not_admin(request):
	if request.user.is_authenticated:
		if not request.user.is_staff:
			raise Http404
	else:
		raise Http404


# Send an email to (my account...for now) that has all the information
# for a user to successfully log into "their" autograder account.
# This is basically done to confirm with the user that they have an account.
def send_confimation_email(username, password):
	subject = "AUTO_GRADER account created"
	message = "Your new AUTO_GRADER account has been created!\n"
	message += "Username: " + username + "\nPassword:" + password
	sender = 'autograderinstructor@gmail.com'
	# The receivers are currently used just for sending.
	# This will be changed later...
	receivers = ['zairea200@potsdam.edu','demaraj198@potsdam.edu']
	send_mail(subject, message, sender, receivers)


#VIEWS BELOW_________________________________________________________________________________


# View for an admin, when registering a user to the database.
# The user currently has no group associated with it, however,
# this is something that we will add.
def register_account_view(request):
	# USER MUST BE AN ADMIN!!!!!!!!!!!
	error_not_admin(request)

	form = forms.UserRegistrationForm(request.POST or None)
	# Grab the information from the user and make sure that the
	# email field has been filled out successfully.
	if request.POST and form.is_valid():
		email_address = form.cleaned_data['email']
		username = email_address.split('@')[0]
		password = User.objects.make_random_password()
		# Basically, we create the user account and fill in default information
		# so that the admin does not know the password of the user, but we are
		# still able to email all of the needed information to said user.
		user = User.objects.create_user(username=username,
										password=password,
										email=email_address)
		user.save()

		# Handles generic layout of sending emails.
		# Self made method (listed above this view).
		send_confimation_email(username=username, password=password)
		return render(request, 'accounts/registration.html', {'form' : form})

	# This will be changed shortly. Varying on what we choose to do.
	# I will think about if we want to redirect, or have a "add another page".
	# Again...this will come later, it doesn't matter right now.
	return render(request, 'accounts/registration.html', {'form' : form})
