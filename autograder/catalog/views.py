'''
Created by: Chris Stannard
File: catalog/views.py
Description:	contains all views for the catalog/ app.
				These views include things for each model in
				catalog/models.py
Last Edited by:	04/16/2019
Last Edited by: Chris Stannard
'''
from django.views import generic
from django import forms
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from catalog.models import Course, Assignment, Instruct, Take
from catalog.forms import CourseForm
from django.contrib.auth.models import User


# This is the view for the location of a user's classes and thing of that sort.
# If you are logged in, you get sent to the page.
# Not logged in? Then you redirected to the login page. Upon logging, you are
# then directed back to the page you were trying to
@login_required
def my_view(request):
	course_list = Course.objects.all()
	instruct = Instruct.objects.all()
	assignment = Assignment.objects.all()
	context = {
		'course_list': course_list,
		'instruct': instruct,
		'assignments': assignment,
	}
	return render(request, 'catalog/my.html', context=context)

def course_new_view(request):
	form = CourseForm()
	if request.method == "POST":
		form = CourseForm(request.POST)
		if form.is_valid():
			course = form.save(commit=True)
			confirmation_message = "Course information updated successfully!"
			return HttpResponseRedirect(reverse('catalog-course_detail', kwargs={'pk':course.id}))
	return render(request, 'catalog/course_new.html', {'form': form})

def course_update_view(request, pk):
	course = Course.objects.get(id=pk)
	form = CourseForm(instance=course)
	if request.method == "POST":
		form = CourseForm(request.POST,instance=course)
		if form.is_valid():
			form.save(commit=True)
			confirmation_message = "Course information updated successfully!"
			return HttpResponseRedirect(reverse('catalog-course_detail', kwargs={'pk':course.id}))
	else:
		form=CourseForm(instance=course)
	context = {
		'form': form,
        'course_instance': course,
	}
	return render(request, 'catalog/course_update.html', {'form': form}, context)


class CourseListView(generic.ListView):
	model = Course
	template = 'catalog/course_list.html'


class CourseDetailView(generic.DetailView):
	model = Course
	template = 'catalog/course_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['instruct'] = Instruct.objects.all()
		context['assignments'] = Assignment.objects.all()
		return context


class AssignmentListView(generic.ListView):
	model = Assignment
	template = 'catalog/assignment_list.html'


class AssignmentDetailView(generic.DetailView):
	model = Assignment
	template = 'catalog/assignment_detail.html'
