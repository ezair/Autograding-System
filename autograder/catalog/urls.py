'''
Created by: Chris S
File: catalog/urls.py
Description: contains all url/path and logic in regards
			 to routing for the catalog application.
Last edited by: Chris Stannard
Last edited on:	04/08/2019
'''
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


# Stick to the nameing conventions for the name= parameter.
# it is always 'app_name-html_file_name' and nothing else.
urlpatterns = [
	path('', views.my_view, name="catalog-my"),
	path('my/', views.my_view, name="catalog-my"),
	path('my/courses/', views.CourseListView.as_view(), name='courses'),
	path('course/<int:pk>', views.CourseDetailView.as_view(), name='course_detail'),
	path('assignment/<int:pk>', views.AssignmentDetailView.as_view(), name='assignment_detail'),
]
