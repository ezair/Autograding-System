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
admin.site.register(Project)
admin.site.register(TestCase)
admin.site.register(Course)

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'assigned_student', 'due_date')

@admin.register(Instruct)
class InstructAdmin(admin.ModelAdmin):
    list_display = ('instructor', 'course')

@admin.register(Take)
class TakeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course')

@admin.register(Grade)
class InstructAdmin(admin.ModelAdmin):
    list_display = ('grader', 'course')
