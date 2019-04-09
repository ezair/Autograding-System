'''
Created by: Chris Stannard
File: catalog/views.py
Description:	contains all views for the catalog/ app.
				These views include things for each model in
				catalog/models.py
Last Edited by:	04/08/2019
Last Edited by: Chris Stannard
'''
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from catalog.models import Course, Instruct
from django.contrib.auth.models import User

# This is the view for the location of a user's classes and thing of that sort.
# If you are logged in, you get sent to the page.
# Not logged in? Then you redirected to the login page. Upon logging, you are
# then directed back to the page you were trying to
@login_required
def my_view(request):
	context = {
	# Why is this here @anyone???
	}
	return render(request, 'catalog/my.html', context=context)


class CourseListView(generic.ListView):
	model = Course
	template = 'catalog/course_list.html'

class CourseDetailView(generic.DetailView):
    model = Course
    template = 'catalog/course_detail.html'