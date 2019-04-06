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


# Simple form that is used for admin's to enter a soon to be user's
# email address, and create it.
# (Group may be added as an additional drop down option for the soon
# to be user).
class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email',]