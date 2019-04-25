'''
Created by:	Eric Zair
File:	submission_grader/admin.py
Description:	Register all models for here that have to do
				with submission_grader application.
Last Edited on: 04/25/2019
Last Edited by:	Eric Zair
'''

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Submission)