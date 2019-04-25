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
	
	class Meta:
		model = Submission
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(SubmissionUploadForm, self).__init__(*args, **kwargs)
		self.fields.pop('assignment', 'submitted_at',)