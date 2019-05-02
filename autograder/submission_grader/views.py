'''
Created by:	Eric Zair
File:	submission_grader/views.py
Description:	Contains all views/pages used for the submission_grader app
				These views will include things like students submitting
				things to git and such.
Last Edited on: 05/1/2019
Last Edited by:	Eric Zair
'''
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from accounts.views import not_instructor_throw_error
from . import forms
from . import models
from catalog.models import Assignment, Project
from datetime import datetime
from django.views.generic import DeleteView, DetailView
from django.urls import reverse_lazy


@login_required
# View page for when a student submits an assignment.
def submit_view(request, pk):
	# We need to account for if the assignment even exists in the first place.
	if not Assignment.objects.filter(project=pk, assigned_student=request.user).exists():
		raise Http404

	# Aye, so the assignment does exist, so we take the firsts one in existance, m8.
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
			return HttpResponseRedirect('/catalog/')
	# When we start handling newer submissions, this will have to be changed.
	form = forms.SubmissionUploadForm(student=request.user,
									  assignment=assignment,
									  files=request.FILES,
									  submitted_at=datetime.now)
	return render(request, 'submission_grader/submit.html', {'form': form})


class DeleteSubmissionView(DeleteView):
	model = models.Submission
	template = 'submission_confirm_delete'
	success_url = reverse_lazy('catalog-courses')

	#def get_success_url(self):
	# 	submission = self.object
	# 	return reverse_lazy('catalog-assignment_detail',
	# 						kwargs={'pk': self.object.pk})


class SubmissionDetailView(DetailView):
	model = models.Submission
	template = 'submission_grader/submission_detail.html'

	def get_success_url(self):
		submission = self.object
		return reverse_lazy('submission_grader-submission_detail',
							 kwargs={'pk': self.object.pk})