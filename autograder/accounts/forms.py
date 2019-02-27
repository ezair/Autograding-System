'''
Created by:	Eric Zair
File:	accounts/admin
Description:	File contains form classes used for all account apps
				related things
				e.g.
					registrating a user account
Created by:	Eric Zair
Last edited on:	02/27/2019
'''
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


# This form is used for the purpose of OVERRIDING
# the user object's fields.
# In otherwords, this form can allow you to add
# MORE fields to user objects for the sake of user registraion.
# Currently, we only have fields for (username, email,
#									  password1, password2).
class CustomUserCreationForm(UserCreationForm):
    # "reads" data off the original user registration model
    # as meta data (data on top of data) and adds email form.
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


# Allows us to override and actually CHANGE
# our custom user fields.
# DON'T EDIT THIS.
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')