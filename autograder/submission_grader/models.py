'''
Created by:	Eric Zair
File:	submission_grader/models.py
Description:	Contains all models for submission_grader
				app.
Last Edited on: 04/24/2019
Last Edited by:	Eric Zair
'''
from django.db import models

class Submission(models.Model):
	assignment = models.ForeignKey('catalog.Assignment', on_delete=models.SET_NULL, null=True)
	submitted_at = models.DateField(auto_now_add=True, blank=True)
	files = models.FileField(upload_to='', help_text='Submit', null=True)

	def __str__(self):
		return "temp for now"