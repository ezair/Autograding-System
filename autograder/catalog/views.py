'''
Created by: Chris Stannard
File: catalog/views.py
Description:	contains all views for the catalog/ app.
				These views include things for each model in
				catalog/models.py
Last Edited by:	05/05/2019
Last Edited by: Eric Zair
'''
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from catalog.models import Course, Assignment, Instruct, Take, Grade
from submission_grader.models import Submission
from catalog.forms import CourseForm
from django.contrib.auth.models import User
from accounts.views import not_instructor_throw_error
from django.utils.decorators import method_decorator


# This is the view for the location of a user's classes and thing of that sort.
# If you are logged in, you get sent to the page.
# Not logged in? Then you redirected to the login page. Upon logging, you are
# then directed back to the page you were trying to
@login_required
def my_view(request):
	take = Take.objects.all()
	instruct = Instruct.objects.all()
	assignment = Assignment.objects.order_by('due_date')[:6]
	context = {
		'take': take,
		'instruct': instruct,
		'assignment': assignment,
	}
	return render(request, 'catalog/my.html', context=context)


# This is the view for course creation for instructors to make thier courses
@login_required
def course_new_view(request):
	# You need to be an instructor to see this page.
	not_instructor_throw_error(request.user)
	# get the course form
	form = CourseForm()
	if request.method == "POST":
		form = CourseForm(request.POST)
		if form.is_valid():
			# creates the course
			course = form.save(commit=True)
			# the creator instructs the course
			Instruct.objects.create(instructor=request.user, course=course).save()
			# and becomes a grader for the course
			Grade.objects.create(grader=request.user, course=course).save()
			# redirect to the newly created course
			return HttpResponseRedirect(reverse('catalog-course_detail', kwargs={'pk':course.id}))
	return render(request, 'catalog/course_new.html', {'form': form})


@login_required
def course_update_view(request, pk):
	# You need to be an instructor to see this page.
	not_instructor_throw_error(request.user)

	course = Course.objects.get(id=pk)
	form = CourseForm(instance=course)
	if request.method == "POST":
		form = CourseForm(request.POST,instance=course)
		if form.is_valid():
			form.save(commit=True)
			confirmation_message = "Course information updated successfully!"
			return HttpResponseRedirect(reverse('catalog-course_detail', kwargs={'pk':course.id}))
	else:
		form = CourseForm(instance=course)
	context = {
		'form': form,
        'course_instance': course,
	}
	return render(request, 'catalog/course_update.html', {'form': form}, context)


# This is where students will view the courses that THEY are taking.
# This does NOT display every single course in the database.
class CourseListView(ListView):
	model = Course
	template = 'catalog/course_list.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['instruct'] = Instruct.objects.all()
		return context


# ...pretty straight forward view.
class CourseDetailView(DetailView):
	model = Course
	template = 'catalog/course_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['instruct'] = Instruct.objects.all()
		context['assignments'] = Assignment.objects.all()
		return context

	# Overide so that a user must be logged in to see this view.
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(CourseDetailView, self).dispatch(*args, **kwargs)


# List all of the assignments that the student is taking.
# ONLY SHOWS ASSIGNMENTS THEY ARE TAKING NOT ALL ASSINGMENTS.
class AssignmentListView(ListView):
	model = Assignment
	template = 'catalog/assignment_list.html'

	# User must be logged in to see this page.
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AssignmentListView, self).dispatch(*args, **kwargs)


# This is where a student will view the content of their assingment
# as well as where their submissions will be listed.
class AssignmentDetailView(DetailView):
	model = Assignment
	template = 'catalog/assignment_detail.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['submission_list'] = Submission.objects.all()
		return context

	# User must be logged in to see this page.
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(AssignmentDetailView, self).dispatch(*args, **kwargs)