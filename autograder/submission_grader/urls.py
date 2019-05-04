from django.urls import path, include
from .views import *
from . import views

urlpatterns = [
	path('assignment/<int:pk>/submit/', submit_view, name='submission_grader-submit'),
	path('assignment/<int:pk>/delete/',
		 DeleteSubmissionView.as_view(),
		 name='submission_grader-submission_confirm_delete'),
	path('submissions/', views.SubmissionListView.as_view(), name='submission_grader-submission_list'),

	#ignore for now.
	path('submission/<int:pk>',
		 SubmissionDetailView.as_view(),
		 name='submission_grader-submission_detail')
]
