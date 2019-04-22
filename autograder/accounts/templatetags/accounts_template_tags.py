'''
Created by:	Eric Zair
File:	accounts/acconts_templates/accouts_template_tags.py
Description:	This file contains CUSTOM made template tags for things like
				checking to see if a user is in a certain group.
				Anything related to user permission handling tags will be
				done in this specific file.

				IMPORTANT NOTE:	If you want to any of these tags into a html file
								then you must add the following in said file:
								"{% load accounts_template_tags %}"
								...don't actually add the quotes with it...
Last edited by:	Eric Zair
Last edited on:	04/22/2019
'''
from django import template


# Instance created so that we can create custom templates tags.
# Template tags in this app will have respect to user's and permissons.
# An example of this being checking to see what group a user is in.
register = template.Library()

# This method is used so that in our html template tags
# we can check to see what group a user is in.
# Useful for front-end querying.
@register.filter(name='has_group')
def has_group(user, group_name):
	return user.groups.filter(name=group_name).exists()