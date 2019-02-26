'''
Created by: Eric Zair
File: accounts/apps.py
Description:	Contains app configuration and rules for
				our Accounts application.
Last edited by: Eric Zair
Last edited on: 02/25/2019
'''
from django.apps import AppConfig


# This needs to be created becasue it is required to give to settings.py
# The exact link that must be given to settings.py (so that it can detect this app)
# can be found in ./__init__.py
class AccountsConfig(AppConfig):
	name = 'accounts'
	verbose_name = "Accounts"