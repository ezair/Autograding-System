'''
Created by: Chris Stannard
File:   catalog/admin.py
Description:    This file handles all of the stuff with respect
                to how you can manipulate and edit catalog related models
                in the django admin page.
Last edited by: Eric Zair
Last edited on: 04/24/2019
'''
from django.contrib import admin
from catalog.models import *


# All we are doing here is adding the option to create the following gorups
# in the /admin page.
admin.site.register(Assignment)
admin.site.register(Project)
admin.site.register(TestCase)
admin.site.register(Course)
admin.site.register(Take)
admin.site.register(Instruct)
admin.site.register(Grade)