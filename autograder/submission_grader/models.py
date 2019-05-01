'''
Created by:	Eric Zair
File:	submission_grader/models.py
Description:	Contains all models for submission_grader
				app.
Last Edited on: 04/24/2019
Last Edited by:	Eric Zair
'''
from django.db import models
from django.core.validators import FileExtensionValidator
import datetime
from django.utils import timezone

# This will return the location that a submission will be stored in.
#The format is:
#				assignment_primary_key/student_username
def get_files_path(submission, filename):
	path = str(submission.assignment) + '/' + str(submission.student) 
	path += '/' + str(submission) + '/' + filename
	return path


# When a student submits a project for a given assignment, we must store it in the
# database of course...hence this Submission model.
class Submission(models.Model):
	assignment = models.ForeignKey('catalog.Assignment', on_delete=models.SET_NULL, null=True)
	submitted_at = models.DateField(default=datetime.datetime.now, blank=True)
	student =  models.ForeignKey("auth.User",
                                 limit_choices_to={'groups__name': "Student"},
                                 on_delete=models.SET_NULL, null=True)
	# only allowed extensions are .zip and .java
	files = models.FileField(upload_to=get_files_path,
							 null=True,
							 max_length=255,
							 validators=[FileExtensionValidator(allowed_extensions=['zip', 'java'])])

	def __str__(self):
		str_ = str(self.student) + " submitted to " + str(self.files)
		return str_ + " at " + str(self.submitted_at)

		# will need a detail page at some point soon.