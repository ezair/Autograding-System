'''
Created by:	Eric Zair
File: accounts/urls.py
Description:	Contains and manages the paths to all of our pages in
				the accounts/ application.
				This will include things like logins, logouts, student registrations,
				...etc
Last edited by:	Jared DeMarais
Last edited on:	04/09/2019
'''
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from . import views


# Linking of all /accounts application pages here.
# Make sure to add the name = param, or everything will just suck.
urlpatterns = [
	path('register/', views.register_account_view, name='accounts-registration'),
	path('login/', LoginView.as_view(template_name='accounts/login.html'),
									 name='accounts-login'),
	path('logout/', LogoutView.as_view(template_name='accounts/logout.html'),
									   name='accounts-logout'),
	path('change/', PasswordChangeView.as_view(template_name='accounts/password_change.html'),
											   name='accounts-password_change'),
	path('change/done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
													    name='password_change_done'),
	path('reset/', PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='accounts-password_reset'),
	path('reset/done', PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
														name='password_reset_done'),
	path('reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
														name='password_reset_confirm'),
	path('reset/complete', PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
														name='password_reset_complete'),
]
