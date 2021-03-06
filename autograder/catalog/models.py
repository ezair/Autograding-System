'''
Created by: Chris S
File: catalog/models.py
Description: contains all url/path and logic in regards
			 to routing for the catalog application.
Last edited by: Eric Zair
Last edited on:	04/24/2019
'''
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.db import models
import datetime


# This model represents a class that a student is taking.
class Course(models.Model):
	name = models.CharField(max_length=80, help_text='Enter course title', default='course')
	crn = models.CharField(max_length=6, help_text='Enter course title', default='00000', unique=True)
	description = models.TextField(help_text='Enter a detailed description', default='This class description')

	def __str__(self):
		return self.name

	# This is the url for the detail view location.
	def get_absolute_url(self):
		return reverse('catalog-course_detail', args=[str(self.id)])


# This model is used to keep tracks of the students that are taking a course.
# Essentially, all we are doing is connecting a student to a course via a student's
# Primary Key.
class Take(models.Model):
    student =  models.ForeignKey("auth.User",
                                 limit_choices_to={'groups__name': "Student"},
                                 on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)

    def __str__(self):
    	return str(self.student) + " is taking " + str(self.course)


# This model connects a instructor to a course via the instructors primary Key
# and the primary key of the course.
class Instruct(models.Model):
    instructor =  models.ForeignKey("auth.User",
                                    limit_choices_to={'groups__name': "Instructor"},
                                    on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)

    def __str__(self):
    	return str(self.instructor) + " instructing " + str(self.course)


# This model connects a grader to a course via the instructors primary Key
# and the primary key of the course.
class Grade(models.Model):
    grader =  models.ForeignKey("auth.User",
                                limit_choices_to={'groups__name': "Grader"},
                                on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.grader) + " grading " + str(self.course)


class MasterAssignment(models.Model):
	name = models.CharField(max_length=60, help_text='Enter a name')
	course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.name

		# This is the url for the submissions list location.
	def get_absolute_url(self):
		return reverse('submission_grader-master_assignment_detail', args=[str(self.id)])


# Model containting one or multiple projects, that a student must submit for a grade.
# Assignment is going to be created by an instructor.
class Assignment(models.Model):
	name = models.CharField(max_length=60, help_text='Enter a name')
	course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
	due_date = models.DateField(null=True, blank=True)
	assigned_student = models.ForeignKey("auth.user",
										 help_text='Assign students to assignment',
										 limit_choices_to={'groups__name': "Student"},
										 on_delete=models.SET_NULL,
										 null=True)
	project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)
	master = models.ForeignKey('MasterAssignment', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.name

	# This is the url for the detail view location.
	def get_absolute_url(self):
		return reverse('catalog-assignment_detail', args=[str(self.id)])


# At its core, this is a one prograamming assignment that will be given to an
# Assignment model.
# Connects to assignment model via Assignment.
class Project(models.Model):
    short_description = models.CharField(max_length=60, help_text='Enter a short description')
    long_description = models.TextField(help_text='Enter a detailed description')

    def __str__(self):
        return self.short_description


# Function used to acutally find the location of a .zip testfiles.
# THIS IS CALLED IN THE TESTCASE MODEL. DON'T CHANGE IT.
# path is: testcases/test case's primary key/file/submitted_at time.
def get_files_path(test_case, filename):
	str_ = "testcases/" + str(test_case.pk) + "/" + str(filename)
	str_ += "/" + str(test_case.submitted_at) + "/" + str(test_case.test_file)
	return str_

# MORE ON THIS LATER.
class TestCase(models.Model):
    submitted_at = models.DateField(default=datetime.datetime.now, blank=True)
    # only .zip files are allowed.
    test_file = models.FileField(upload_to=get_files_path,
    							 null=True,
    							 max_length=255,
    							 validators=[FileExtensionValidator(allowed_extensions=['zip'])])
    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)

    def file_name(self):
    	str_ = self.test_file.path
    	return str_[str_.rindex('/') + 1 : len(str_)]

    def get_abs_path(self):
    	return str(self.test_file.path)

    def __str__(self):
        return str(self.test_file) + " for project " + str(self.project)