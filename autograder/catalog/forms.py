'''
Created by: Chris S
File: catalog/forms.py
Description: contains the forms for the catalog application.
Last edited by: Chris Stannard
Last edited on:	04/16/2019
'''

from django import forms
from catalog.models import Course, Assignment

class CourseForm(forms.ModelForm):
    class Meta():
        model = Course
        fields = ['name','crn','description']

class AssignmentForm(forms.ModelForm):
    class Meta():
        model = Assignment
        fields = ['name', 'course', 'project', 'due_date']
