from django.urls import path, include
from . import views

urlpatterns = [
	path('submit/', views.submit_view, name='submission_grader-submit')
]