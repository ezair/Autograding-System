'''
Created by:	Chris Stannard
File:	catalog/template_tags/catalog_template_tags.py
Description:	This file contains CUSTOM made template tags for things like
				filtering through models.

				IMPORTANT NOTE:	If you want to any of these tags into a html file
								then you must add the following in said file:
								"{% load catalog_template_tags %}"
								...don't actually add the quotes with it...
Last edited by:	Chris Stannard
Last edited on:	05/15/2019
'''
from django import template
from catalog.models import Instruct, Grade, MasterAssignment, TestCase
import datetime
import os
import shutil
import zipfile


# needed so that template tags are actually usable.
register = template.Library()

# Finds all the courses an instructor instructs
@register.filter(name='instructor_courses')
def instructor_courses(instructor):
    instructs = Instruct.objects.filter(instructor = instructor)
    courses = []
    for instruct in instructs:
        courses.append(instruct.course)
    return courses

# Finds all master assignments for a course
@register.filter(name='get_master_assignment')
def get_master_assignment(course):
    return MasterAssignment.objects.filter(course = course)

# Finds all assignments that the user can grade
@register.filter(name='get_all_my_grading_assignments')
def get_all_my_grading_assignments(user):
	assignments = []
	my_grading_courses = Grade.objects.filter(grader = user)
	for grading in my_grading_courses:
		for assignment in get_master_assignment(grading.course):
			assignments.append(assignment)
	return assignments

# finds the instructors for a course
@register.filter(name='get_instructor')
def get_instructor(course):
	instructs = Instruct.objects.filter(course = course)
	instructors = []
	for instruct in instructs:
		instructors.append(instruct.instructor)
	return instructors

# Finds courses that the user grades but doesn't instructs
@register.filter(name='grading_courses')
def grading_courses(user):
	all_grading = Grade.objects.filter(grader = user)
	not_my_courses = []
	for grading in all_grading:
		if Instruct.objects.filter(course = grading.course, instructor = grading.grader).exists():
			pass
		else:
			not_my_courses.append(grading.course)
	return not_my_courses


@register.filter(name='run_gradle')
def run_gradle(submission):
	# Need to find location of test files, so they can be copied over later.
	test_case = TestCase.objects.get(project=submission.assignment.project.pk)
	print(type(test_case))
	# We need to create the dir/ that gradle will be located in.
	# Then, we will proceed to create a .gradle in that location.
	# We then need to move to that location in our server, so we can
	# later run the gradle build command.
	submission_location = submission.files.path
	test_case_location = test_case.get_abs_path()
	new_dir_name = "compiler/" + str(submission)
	os.mkdir("/code/" + new_dir_name)
	os.chdir("/code/" + new_dir_name)
	os.system("gradle init")
	# We need to edit the build file, so that it has the correct dependencies.
	with open('./build.gradle', 'w') as build_file:
		build_file.write("apply plugin: 'java'\n")
		build_file.write("repositories {\nmavenCentral()\n}\n")
		build_file.write("dependencies {\ntestCompile group: 'junit', name: 'junit', version: '4+'\n}")

	# We need the correct directories, so we that we can copy the test_case files & submission
	# files to the location where gradle can actually find them.
	os.mkdir("src/")
	os.mkdir("src/main/")
	os.mkdir("src/test/")
	shutil.copy(submission_location, "./src/main/")
	shutil.copy(test_case_location, "./src/test/")

	# Need to unzip these bad bois into their respective folders.
	zip_file = zipfile.ZipFile("./src/main/" + submission.file_name(), 'r')
	zip_file.extractall('./src/main/')
	zip_file = zipfile.ZipFile("./src/test/" + test_case.file_name(), 'r')
	zip_file.extractall('./src/test/')
	zip_file.close()

	# Finally, we will now compile all the java files, so that it creates
	# the "reports/" directory where "index.html" will be located.
	os.system("gradle build")
	os.chdir("/code")
	# This is the path to the "index.html" file after the build is done.
	return "code/" + new_dir_name + "/build/reports/tests/test/index.html"

@register.filter(name='grade_exists')
def grade_exists(submission):
	new_dir_name ="compiler/" + str(submission)
	return os.path.isfile("./" + new_dir_name + "/build/reports/tests/test/index.html")

@register.filter(name='grade_path')
def grade_path(submission):
	new_dir_name ="compiler/" + str(submission)
	if os.path.isfile("./" + new_dir_name + "/build/reports/tests/test/index.html"):
		return "./" + new_dir_name + "/build/reports/tests/test/index.html"
