'''
Created by: Eric Zair
File: accounts/models.py
Description: Contains all information regarding our database
			 models withr respects to the accounts application.
Last edited by: Eric Zair
Last edited on:	04/15/2019
'''
from django.db import models
from django.contrib.auth.models import Group, User
from django.urls import reverse
from catalog.models import Course


class Invite(models.Model):
	# Used do add a drop down for deciding for what group to add a user to.
	# Instructor that wants to send the invite.
	# Can also be an admin.
	GROUP_CHOICES = (('Student', 'STUDENT'),
					 ('Instructor', 'INSTRUCTOR'),
					 ('Grader', 'GRADER'))

	group_choice = models.CharField(max_length=20, choices=GROUP_CHOICES,
									default=('Student', 'STUDENT'), null=False)

	invite_sender = models.ForeignKey(User, on_delete=models.DO_NOTHING,
							   		  to_field='username', null=True,
								 	  related_name='invite_sender',
								 	  default='autograderinstructor')
	
	# Cascade delete this so that if a user is removed, all fkey records
	# accociated are as well.
	invite_receiver = models.ForeignKey(User, on_delete=models.CASCADE,
										to_field='username', null=True,
										related_name='invite_receiver')
	# This is the course that you would like to invite a grader.
	# or an instructor to.
	course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
	#stamp/log the time a that the invite was made,
	# for the admin to have record.
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		str_ = str(self.invite_sender) + " invited "
		str_ += str(self.invite_receiver) + " to " + str(self.course)
		return str_