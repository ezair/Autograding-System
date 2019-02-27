'''
Created by:	Eric Zair
File:	accounts/admin.py
Description:	This file contains anything regarding the admin
				account configureation.
				E.g. Overriding the field for Admin registration
				and such.
Last edited by:	Eric Zair
Last edited on:	02/27/2019
'''
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser


# Override the default admin user by adding an email field
# to be filled out.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]


# Allows you to create an admin user from the /admin page.
# Should not be changed.
admin.site.register(CustomUser, CustomUserAdmin)