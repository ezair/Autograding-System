'''
Created by:	Eric Zair
File:	accounts/admin
Description:	File contains form classes used for all account apps
				related things
				e.g.
					admin registrating a user account 
Created by:	Eric Zair
Last edited on:	02/27/2019
'''
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from .models import *

# Simple form that is used for admin's to enter a soon to be user's
# email address, and create it.
# (Group may be added as an additional drop down option for the soon
# to be user).
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


# Form that will have a dropdown menu for selecting a group option
# The instructor can then add a list of users to a course given by
# a dropdown menu.
class InviteForm(forms.ModelForm):
	# Field used to grab multiple usernames sperated by a ';'.
	receiver_usernames = forms.CharField(help_text='Enter emails separated by a semi-colin',
									 	 required = True)
	class Meta:
		model = Invite
		fields = ('invite_sender', 'receiver_usernames', 'course', 'group_choice')
		
	def clean_receiver_usernames(self):
		cleaned_data = self.cleaned_data['receiver_usernames']
		# Individually grab each username, seperated by a semi-colon.
		#for username in receiver_usernames:
		return cleaned_data
	
	def __init__(self, *args, **kwargs):
		# we want to references the 'invite_sender' field, but not
		# a field for the user to enter
		super(InviteForm, self).__init__(*args, **kwargs)
		self.fields.pop('invite_sender')