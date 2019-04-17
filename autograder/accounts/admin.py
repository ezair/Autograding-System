'''
Created by: Eric Zair
File:   accounts/admin.py
Description:    This file handles all of the stuff with respect
                to how you can manipulate and edit accounts/ related models
                in the django admin page.
Last edited by: Eric Zair
Last edited on: 04/17/2019
'''
from django.contrib import admin
from accounts.models import *


# All we are doing here is adding the option to create the following models.
# in the /admin page.
admin.site.register(Invite)