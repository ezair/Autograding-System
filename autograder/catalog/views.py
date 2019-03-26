'''
Created by: Chris Stannard
File: catalog/views.py
Description:	contains all views for the catalog/ app.
				These views include things for each model in
				catalog/models.py
Last Edited by:	03/23/2019
Last Edited by: Eric Zair
'''

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# This is the view for the location of a user's classes and thing of that sort.
# If you are logged in, you get sent to the page.
# Not logged in? Then you redirected to the login page. Upon logging, you are
# then directed back to the page you were trying to
@login_required
def my_view(request):	
    	return render(request, 'catalog/my.html')

@login_required(login_url='/catalog/')
def logout_view(request):
	logout(request)
	# Redirect to a success page.
	return render(request, 'catalog/logout.html')
