from django.urls import path, include
from .views import *

urlpatterns = [
	path('project/<int:pk>/submit/', submit_view, name='submission_grader-submit'),
	path('project/<int:pk>/delete/',
		 DeleteSubmissionView.as_view(),
		 name='submission_grader-submission_confirm_delete'),
	path('submission/<int:pk>',
		 SubmissionDetailView.as_view(),
		 name='submission_grader-submission_detail')
]