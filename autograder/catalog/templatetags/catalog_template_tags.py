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

# @register.filter(name='grading_courses')
# def grading_courses(grader):
#     courses_grading = Grade.objects.filter(grader = grader)
#     not_my_courses = []
#     for course_grading in courses_grading:
#         instructor = Instruct.object.get(course = course_grading.course)
#         if instructor != grader:
#             not_my_courses.append(instruct.course)
#     return courses
#
# @register.filter(name='get_course_instructors')
# def get_course_instructors(course):
#     instructors = Instruct(course = course)
#     return instructors
