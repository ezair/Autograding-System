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
Last edited on:	04/09/2019
'''
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.http import Http404
from . import forms
from catalog import models


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
	message += "Username: " + username + "\nPassword: " + password
	sender = 'autograderinstructor@gmail.com'
	# The receivers are currently used just for sending.
	# This will be changed later...
	receivers = ['zairea200@potsdam.edu','demaraj198@potsdam.edu']
	password_reset_link = 'Please reset your password at http://127.0.0.1:8000/accounts/change/'
	message += "\n" + password_reset_link
	# Attach password change link, so user can change their password to their liking.
	email = EmailMultiAlternatives(subject, message, sender, receivers)
	email.send()


# Send email to user that verifies they are now in a course.
def send_join_course_email(invite_receivers, course, group,
						   invite_sender='autograderinstructor@gmail.com'):
	subject = "Welcome to " + course + "."
	message = "You have been registered to join " + str(course)
	message += " as a " + str(group) + "."
	# Currently this works (sends an email to 1 student), but eventually
	# it will work for multiple.
	for i in range(len(invite_receivers)):
		invite_receivers[i] += "@potsdam.edu"
	email = EmailMultiAlternatives(subject, message, invite_sender, invite_receivers)
	email.send()


# parses data given by a django form object.
# We then create a user account based off of that form.
def register_user_account(form):
	username = form.cleaned_data['username']
	email_address = str(username) + '@potsdam.edu'
	password = User.objects.make_random_password()
	# We NEED to make sure that we are NOT trying to create a duplicate user
	# accounts. Because that just sucks. Like omg it really sucks. 
	# It's actually not fun at all.
	if not User.objects.filter(username=username).exists():
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


#VIEWS BELOW_________________________________________________________________________________

# View for an admin, when registering a user to the database.
def register_account_view(request):
	# USER MUST BE AN ADMIN, or they should not be creating other users
	error_not_admin(request)
	form = forms.UserRegistrationForm(request.POST or request.GET or None)
	# Grab the information from the user and make sure that the
	# email field has been filled out successfully.
	if request.POST and form.is_valid():
		register_user_account(form)
		return render(request, 'accounts/registration.html', {'form' : form})
	# Not sure where we want to redirect quite yet.
	return render(request, 'accounts/registration.html', {'form' : form})


@login_required()
def make_invite_view(request):
	form = forms.InviteForm(request.POST or request.GET or None)

	if request.POST and form.is_valid():
		# Rather than parsing these several times, we do it once in the beginning.
		invite_receiver = form.cleaned_data['invite_receiver']
		course = form.cleaned_data['course']
		add_to_group = form.cleaned_data['group_choice']
	
		# We need to create the appropriate model for
		# the approriate group given in the view dropdown menu.
		if add_to_group == 'Student':
			# We only want to add a student to the course, if the record does not exist.
			if not models.Take.objects.filter(student=invite_receiver, course=course).exists():
				models.Take.objects.create(student=invite_receiver, course=course).save()

		# THIS WILL ALSO ADD INSTRUCTOR TO GRADER ROLE BY DEFAULT....eventually...
		elif add_to_group == 'Instructor':
			# We only want to make a instructor, if the record does not already exist.
			if not models.Instruct.objects.filter(instructor=invite_receiver, course=course).exists():
				models.Instruct.objects.create(instructor=invite_receiver, course=course).save()
		
		# Form is valid, so we store into our database, and then email the user.
		form.save()
		send_join_course_email(invite_receivers=[str(invite_receiver)],
							   course=str(course), group=add_to_group)

		# Make sure the user is actually registered to the proper group.
		# Even if they are in the group already, we do this to be safe.
		group = Group.objects.get(name=str(add_to_group))
		group.user_set.add(invite_receiver)

		return render(request, 'accounts/make_invite.html', {'form' : form})
	
	# Have not decided if we want to redirect the page, or just yield a
	# pop up message. TBA.
	return render(request, 'accounts/make_invite.html', {'form': form})