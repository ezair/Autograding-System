'''
Created by:	Chris Stannard
File:	catalog/template_tags/catalog_template_tags.py
Description:	This file contains CUSTOM made template tags for things like
				filtering through models.

				IMPORTANT NOTE:	If you want to any of these tags into a html file
								then you must add the following in said file:
								"{% load accounts_template_tags %}"
								...don't actually add the quotes with it...
Last edited by:	Chris Stannard
Last edited on:	05/9/2019
'''
from django import template
from catalog.models import Instruct, Grade, MasterAssignment
import datetime
import os

register = template.Library()


@register.filter(name='instructor_courses')
def instructor_courses(instructor):
    instructs = Instruct.objects.filter(instructor = instructor)
    courses = []
    for instruct in instructs:
        courses.append(instruct.course)
    return courses

@register.filter(name='get_master_assignment')
def get_master_assignment(course):
    return MasterAssignment.objects.filter(course = course)

@register.filter(name='get_all_my_grading_assignments')
def get_all_my_grading_assignments(user):
	assignments = []
	my_grading_courses = Grade.objects.filter(grader = user)
	for grading in my_grading_courses:
		for assignment in get_master_assignment(grading.course):
			assignments.append(assignment)
	return assignments

@register.filter(name='get_instructor')
def get_instructor(course):
	instructs = Instruct.objects.filter(course = course)
	instructors = []
	for instruct in instructs:
		instructors.append(instruct.instructor)
	return instructors

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

	return 0
#
# @register.filter(name='get_course_instructors')
# def get_course_instructors(course):
#     instructors = Instruct(course = course)
#     return instructors
