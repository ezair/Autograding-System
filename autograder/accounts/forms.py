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
        fields = ['email']


class InviteForm(forms.ModelForm):
	class Meta:
		model = Invite
		fields = '__all__'
		exclude = ['invite_sender',]

	# Created the invite form object.
	# The sender and course will be filled in by default,
	# because we will already know them by default.
	# Essentially, there is no need for the user to add them.
	
	# def __init__(self, **kwargs):
	# 	self.invite_sender = kwargs.pop('invite_sender')
	# 	super(InviteForm, self).__init__(*kwargs)


	# upon submission, we add the form to the actual database.
	def save(self, commit=True):
		# we need to set commit=True, since we are populating some
		# forms by default, but don't want to do null=False
		invite = super(InviteForm, self).save(commit=False)
		# Form data is good, so we will save the invitation.
		if commit:

			#make take here??
			invite.save()
		return invite