'''
Created by:	Eric Zair
File:	submission_grader/views.py
Description:	Contains all views/pages used for the submission_grader app
				These views will include things like students submitting
				things to git and such.
Last Edited on: 05/05/2019
Last Edited by:	Eric Zair
'''
from django.views.generic import DeleteView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from accounts.views import not_instructor_throw_error, not_student_throw_error
from django.http import HttpResponseRedirect, Http404
from django.utils.decorators import method_decorator
from catalog.models import Assignment, Project, MasterAssignment
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from datetime import datetime
from . import forms
from . import models


@login_required
# View page for when a student submits an assignment.
def submit_view(request, pk):
	# must be a student to get to this page.
	# otherwise, you get a 404 error.
	not_student_throw_error(request.user)

	# We need to account for if the assignment even exists in the first place.
	if not Assignment.objects.filter(project=pk, assigned_student=request.user).exists():
		raise Http404

	# Aye, so the assignment does exist, so we, pk take the firsts one in existance, m8.
	# We filter it for the first assignment, just incase there is another model of the project.
	# There should NOT EVER BE, but stuff happens.
	assignment = Assignment.objects.filter(project=pk).order_by('id').first()
	if request.method == 'POST':
		form = forms.SubmissionUploadForm(student=request.user,
										  assignment=assignment,
										  files=request.FILES,
										  submitted_at=datetime.now)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('catalog-assignment_detail',
										kwargs={'pk': assignment.pk}))
	# When we start handling newer submissions, this will have to be changed.
	form = forms.SubmissionUploadForm(student=request.user,
									  assignment=assignment,
									  files=request.FILES,
									  submitted_at=datetime.now)
	return render(request, 'submission_grader/submit.html', {'form': form})


# This view brings the user to a page that prompts them to
# confirm that they want to delete a submission.
# They must click "confirm" for the submission to be deleted
class DeleteSubmissionView(DeleteView):
	model = models.Submission
	template = 'submission_confirm_delete'

	def get_success_url(self):
		submission = self.object
		assignment = submission.assignment.pk
		return reverse_lazy('catalog-assignment_detail',
	 						kwargs={'pk': assignment})

	# User must be logged in to see this page.
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(DeleteSubmissionView, self).dispatch(*args, **kwargs)


# NOT SURE IF THIS IS NEEDED OR NOT.
# MORE ON THIS LATER.
class SubmissionDetailView(DetailView):
	model = models.Submission
	template = 'submission_grader/submission_detail.html'

	def get_success_url(self):
		submission = self.object
		return reverse_lazy('submission_grader-submission_detail',
							 kwargs={'pk': self.object.pk})

	# User must be logged in to see this page.
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(SubmissionDetailView, self).dispatch(*args, **kwargs)


# NOTE SURE IF THIS IS NEEDED OR NOT.
# MORE ON THIS LATER.
class MasterAssignmentDetailView(DetailView):
	model = MasterAssignment
	template = 'catalog/masterassignment_detail.html'

	# User must be logged in to see this page.
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(MasterAssignmentDetailView, self).dispatch(*args, **kwargs)