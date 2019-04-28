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
from accounts.views import not_instructor_throw_error
from . import forms
from . import models


@login_required
# View page for when a student submits and assignment.
def submit_view(request):
	form = forms.SubmissionUploadForm(request.POST or None, request.FILES or None)
	
	if request.method == 'POST'and form.is_valid():
			models.Submission(assignment=form.cleaned_data['assignment'],
							  student=request.user,
							  files=form.cleaned_data['files'])
			form.save()
			print("I got here")
			return HttpResponseRedirect('/catalog/')
	return render(request, 'submission_grader/submit.html', {'form': form})
