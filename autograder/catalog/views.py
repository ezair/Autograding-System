from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import Context, loader
from django.contrib.auth.decorators import login_required


# This is the view for the location of a user's classes and thing of that sort.
# If you are logged in, you get sent to the page.
# Not logged in? Then you redirected to the login page. Upon logging, you are
# then directed back to the page you were trying to
@login_required
def my_view(request):
    	template = loader.get_template('catalog/my.html')
    	return HttpResponse(template.render())