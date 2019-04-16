'''
Created by: Chris S
File: catalog/forms.py
Description: contains the forms for the catalog application.
Last edited by: Chris Stannard
Last edited on:	04/15/2019
'''

from django import forms
from catalog.models import Course#, Submission

class CourseUpdateForm(forms.ModelForm):
    class Meta():
        model = Course
        fields = ['name','crn','description']
