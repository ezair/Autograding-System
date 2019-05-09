'''
Created by: Chris S
File: catalog/urls.py
Description: contains all url/path and logic in regards
			 to routing for the catalog application.
Last edited by: Chris Stannard
Last edited on:	04/16/2019
'''
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


# Stick to the nameing conventions for the name= parameter.
# it is always 'app_name-html_file_name' and nothing else.
urlpatterns = [
	path('', views.my_view, name="catalog-my"),
	path('my/', views.my_view, name="catalog-my"),
	path('my/courses/', views.CourseListView.as_view(), name='catalog-courses'),
	path('course/new', views.course_new_view, name='catalog-course_new'),
	path('course/<int:pk>', views.CourseDetailView.as_view(), name='catalog-course_detail'),
	path('course/<int:pk>/update', views.course_update_view, name='catalog-course_update'),
	path('my/assignments/', views.AssignmentListView.as_view(), name='catalog-assignments'),
	path('assignment/<int:pk>',
		 views.AssignmentDetailView.as_view(),
		 name='catalog-assignment_detail'),

	path('my/instructor_assignments/',
		 views.MasterAssignmentListView.as_view(),
		 name='catalog-master_assignments'),
]
