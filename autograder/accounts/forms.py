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
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


# This form is used for the purpose of OVERRIDING
# the user object's fields.
# In otherwords, this form can allow you to add
# MORE fields to user objects for the sake of user registraion.
# Currently, we only have fields for registration are:
# (username, email, password1, password2).
class StudentRegistrationForm(UserCreationForm):
    # extra datafields go here.
    email = forms.EmailField()

    # Checks to see what model we are basing this form off of,
    # which in this case, is the built in django "User" model.
    # NOTE:
    #	If you want to add anther fiedl to this form, you must add it
    #   to the "fields" list located below in the Meta class.
    class Meta(UserCreationForm):
        model = User
        fields = ['username', 'email', 'password1', 'password2']