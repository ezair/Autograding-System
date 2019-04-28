'''
Created by:	Eric Zair
File:	submission_grader/models.py
Description:	Contains all models for submission_grader
				app.
Last Edited on: 04/24/2019
Last Edited by:	Eric Zair
'''
from django.db import models


# This will return the location that a submission will be stored in.
#The format is:
#				assignment_primary_key/student_username
def get_files_path(submission, filename):
	return str(submission.assignment.pk) + '/' + str(submission.student) + '/' + filename


# When a student submits a project for a given assignment, we must store it in the
# database of course...hence this Submission model.
class Submission(models.Model):
	assignment = models.ForeignKey('catalog.Assignment', on_delete=models.SET_NULL, null=True)
	submitted_at = models.DateField(auto_now_add=True, blank=True)
	student =  models.ForeignKey("auth.User",
                                 limit_choices_to={'groups__name': "Student"},
                                 on_delete=models.SET_NULL, null=True)
	files = models.FileField(upload_to=get_files_path,
							 null=True,
							 max_length=255)

	def __str__(self):
		str_ = str(self.student) + " submitted to " + str(self.files)
		return str_ + " at " + str(self.submitted_at)