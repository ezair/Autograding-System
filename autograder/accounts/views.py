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
Last edited on:	04/24/2019
'''
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.mail import EmailMultiAlternatives
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import Http404
from catalog import models
from .models import Invite
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


# In the event that the user is NOT an instructor, we throw
# then a 403 error message, stating that they cannot go to the given
# page.
def not_instructor_throw_error(user):
	if not user.groups.filter(name='Instructor').exists():
		raise PermissionDenied

# In the event that the user is NOT a STUDENT, we throw
# then a 403 error message, stating that they cannot go to the given
# page.
def not_student_throw_error(user):
	if not user.groups.filter(name='Student').exists():
		raise PermissionDenied	


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
	receivers = [username + '@potsdam.edu']
	password_reset_link = 'Please reset your password at http://127.0.0.1:8000/accounts/change/'
	message += "\n" + password_reset_link
	# Attach password change link, so user can change their password to their liking.
	email = EmailMultiAlternatives(subject, message, sender, receivers)
	email.send()


# Send email to user that verifies they are now in a course.
def send_join_course_email(receiver_username, course, group,
						   invite_sender='autograderinstructor@gmail.com'):
	subject = "Welcome to " + course + "."
	message = "You have been registered to join " + str(course)
	message += " as a " + str(group) + "."
	# Currently this works (sends an email to 1 student), but eventually
	# it will work for multiple.
	email = EmailMultiAlternatives(subject,
								   message,
								   invite_sender,
								   [receiver_username + '@potsdam.edu'])
	email.send()


# Literally creates a user object with a random generated password,
# then saids that user an email stating the account was made.
def register_user_account(username):

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


# User was not yet in the course, so we send the confirmation email
# and add them to the respective group needed.
# Invite model will also be created here, with a record of what happened. 
def invite_successful(receiver_user, sender_user, add_to_group, course):
	send_join_course_email(receiver_username=receiver_user.username,
						   course=str(course),
						   group=add_to_group)
	# Make sure the user is actually registered to the proper group.
	# Even if they are in the group already, we do this to be safe.
	group = Group.objects.get(name=add_to_group)
	group.user_set.add(receiver_user)
	Invite.objects.create(group_choice=add_to_group,
						  invite_sender=sender_user,
						  invite_receiver=receiver_user,
						  course=course).save()


#VIEWS BELOW_________________________________________________________________________________


# View for an admin, when registering a user to the database.
@login_required()
def register_account_view(request):
	# User must be in instructor group.
	not_instructor_throw_error(request.user)

	form = forms.UserRegistrationForm(request.POST or None)
	# Grab the information from the user and make sure that the
	# email field has been filled out successfully.
	if request.POST and form.is_valid():
		register_user_account(form.cleaned_data['username'])
		return render(request, 'accounts/registration.html', {'form' : form})
	# Not sure where we want to redirect quite yet.
	return render(request, 'accounts/registration.html', {'form' : form})


@login_required()
# View that will allow an instructor to add MULTIPLE users to a group.
# NOTE:	You must be an instructor to see this page ofc.
def make_invite_view(request):
	# Don't want non-instructors to get to this page.
	not_instructor_throw_error(request.user)

	form = forms.InviteForm(request.POST or None)
	
	# In any other case, we simply redirect somewhere else.
	if request.POST and form.is_valid():
		course = form.cleaned_data['course']
		add_to_group = form.cleaned_data['group_choice']

		# Recall: The receiver_usernames field contains multiple
		# usernames, all seperated by a ';'. We have handle each.
		for username in form.cleaned_data['receiver_usernames'].split(';'):	
			# The direct below line is done so that even if a user enters
			# a email instead of a username (by accident), it is parsed out.
			username = username.split('@')[0]
			register_user_account(username)
			user = User.objects.get(username=username)
			
			if add_to_group == 'Student':
				# We only want to add a student to the course, if the record does not exist.
				if not models.Take.objects.filter(student=user, course=course).exists():
					models.Take.objects.create(student=user, course=course).save()
					invite_successful(user, request.user, add_to_group, course)

			elif add_to_group == 'Instructor':
				# We only want to make a instructor, if the record does not already exist.
				if not models.Instruct.objects.filter(instructor=user, course=course).exists():
					models.Instruct.objects.create(instructor=user, course=course).save()
					# Recall: An instructor should always be registered as a grader.
					models.Grade.objects.create(grader=user, course=course).save()			
					invite_successful(user, request.user, add_to_group, course)

			# User must be a grader in this case.
			else:
				if not models.Grade.objects.filter(grader=user, course=course).exists():
					models.Grade.objects.create(grader=user, course=course).save()
					invite_successful(user, request.user, add_to_group, course)

		return render(request, 'accounts/make_invite.html', {'form' : form})
	# Have not decided if we want to redirect the page, or just yield a
	# pop up message. TBA.
	return render(request, 'accounts/make_invite.html', {'form': form})