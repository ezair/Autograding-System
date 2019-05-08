'''
Created by:	Eric Zair
File:	accounts/acconts_templates/accouts_template_tags.py
Description:	This file contains CUSTOM made template tags for things like
				checking to see if a user is in a certain group.
				Anything related to user permission handling tags will be
				done in this specific file.

				IMPORTANT NOTE:	If you want to any of these tags into a html file
								then you must add the following in said file:
								"{% load accounts_template_tags %}"
								...don't actually add the quotes with it...
Last edited by:	Eric Zair
Last edited on:	04/22/2019
'''
from django import template
from submission_grader.models import Submission
import os

# Instance created so that we can create custom templates tags.
# Template tags in this app will have respect to user's and permissons.
# An example of this being checking to see what group a user is in.
register = template.Library()


# This method is used so that in our html template tags
# we can check to see what group a user is in.
# Useful for front-end querying.
@register.filter(name='has_group')
def has_group(user, group_name):
	return user.groups.filter(name=group_name).exists()


# Given an assignment, we can find the last created submission associated
# with it.
@register.filter(name='get_recent_submission')
def get_recent_submission(assignment):
	if Submission.objects.filter(assignment=assignment.pk,
			student=assignment.assigned_student.pk).exists():
		submission = Submission.objects.filter( assignment=assignment.pk,
			student=assignment.assigned_student.pk).order_by('id').last()
		return submission.file_name()
	return "No submissions"


# Given an assignment, we can find the last crated submissions's pk
# associated with it.
@register.filter(name='get_recent_submission_pk')
def get_recent_submission_pk(assignment):
	if Submission.objects.filter(assignment=assignment.pk,
					student=assignment.assigned_student.pk).exists():
		submission = Submission.objects.filter(assignment=assignment.pk,
					student=assignment.assigned_student.pk).order_by('id').last()
		return submission.pk
	return 0


# Given an assignment, we can find the last created submission's path associated
# with it.
@register.filter(name='get_recent_submission_path')
def get_recent_submission_path(assignment):
	if Submission.objects.filter(assignment=assignment.pk,
			student=assignment.assigned_student.pk).exists():
		submission = Submission.objects.filter( assignment=assignment.pk,
			student=assignment.assigned_student.pk).order_by('id').last()
		return submission.files.path
	return "No submissions"


@register.filter(name='get_recent_submission_java_files')
# Grabs all java files that are located inside the recent submission folder.
def get_recent_submission_java_files(assignment):
	# Assuming that submissions exist, we will find ONLY all the associated
	# java files.
	if Submission.objects.filter(assignment=assignment.pk,
			student=assignment.assigned_student.pk).exists():
		submission = Submission.objects.filter( assignment=assignment.pk,
			student=assignment.assigned_student.pk).order_by('id').last()
		all_java_files = []
		for file in os.listdir(submission.submission_folder_path()):
			if file.endswith('.java'):
				all_java_files.append(file)
		# We want to return the set version, so that we can parse through it
		# in .html pages.
		return all_java_files
	return 0;

@register.filter(name='get_recent_submission_folder_path')
def get_recent_submission_folder_path(assignment):
	if Submission.objects.filter(assignment=assignment.pk,
			student=assignment.assigned_student.pk).exists():
		submission = Submission.objects.filter( assignment=assignment.pk,
			student=assignment.assigned_student.pk).order_by('id').last()
		return submission.submission_folder_path()
	return 0

@register.filter(name='get_recent_submission_time')
def get_recent_submission_time(assignment):
	if Submission.objects.filter(assignment=assignment.pk,
			student=assignment.assigned_student.pk).exists():
		submission = Submission.objects.filter( assignment=assignment.pk,
			student=assignment.assigned_student.pk).order_by('id').last()
		return submission.submitted_at
	return 0

# Possibly temp
def some_name_here(assignment_name):
	assignments = Assignment.objects.filter(name=assignment_name,  course=course.pk)
	all_student_submissions = []
	for assignment in assignments:
		if Submission.objects.filter(assignment=assignment.pk,
				student=assignment.assigned_student.pk).exists():
			submission = Submission.objects.filter(assignment=assignment.pk,
				student=assignment.assigned_student.pk).last()
			all_student_submissions.append(submission)
	return all_student_submissions
