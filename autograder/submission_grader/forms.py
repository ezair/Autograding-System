'''
Created by:	Eric Zair
File:	submission_grader/forms.py
Description:	Contains all forms for the submission_grader
				application.
Last edited by:	Eric Zair
Last edited on:	04/25/2019
'''

from django.contrib.auth.models import User
from django import forms
from .models import *


# This will be the form for when a student uploads
# the code they wrote for an assignment.
class SubmissionUploadForm(forms.ModelForm):
	
	class Meta():
		model = Submission
		fields = '__all__'
		exclude = ('assignment', 'student',)

	# Need to access this data, m8.
	def __init__(self, *args, **kwargs):
		self.assignment = kwargs.pop('assignment')
		self.student = kwargs.pop('student')
		super(SubmissionUploadForm, self).__init__(*args, **kwargs)

	# Override the form, so that it gets the args that it needs.
	def save(self, commit=True):
		submission = super(SubmissionUploadForm, self).save(commit=False)
		submission.assignment = self.assignment
		submission.student = self.student
		if commit:
			submission.save()
		return submission