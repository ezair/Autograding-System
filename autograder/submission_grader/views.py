'''
Created by:	Eric Zair
File:	submission_grader/views.py
Description:	Contains all views/pages used for the submission_grader app
				These views will include things like students submitting
				things to git and such.
Last Edited on: 04/25/2019
Last Edited by:	Eric Zair
'''
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.views import not_instructor_throw_error
from django.http import HttpResponseForbidden
from . import forms


@login_required
def submit_view(request):
	if request.method == 'POST':
		form = forms.SubmissionUploadForm(request.POST or request.FILES)
		# TEST STATEMENT
		if form.is_valid():
			form.save()
			return render(request, 'submission_grader/submit.html', {'form': form})
	else:
		form = forms.SubmissionUploadForm()
		if form.is_valid():
			form.save()
			return render(request, 'submission_grader/submit.html', {'form': form})