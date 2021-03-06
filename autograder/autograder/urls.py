"""autograder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


'''
Description:    this is the MAIN urls.py file. It will link all of the paths()
                from every single django application we have created.
Last edited by: Eric Zair
Last edited on: 02/26/2019
'''
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


# Simply contains the paths to different applications in our project.
# This list of urls will ONLY have paths to default apps and to our homepage.
# NOTE:	Path to homepage should be '/'.
#	EVEN MORE IMPORTANT NOTE:
#		When it comes to using the "name=" parameter, always name the link
#		name='application_name-the_name_of_the_template'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('catalog/', include('catalog.urls')),
    path('submission_grader/', include('submission_grader.urls')),
]

# So that we can load static files properly from ALL url locations.
# This DOES NOT need to be added to any other urls.py files.
urlpatterns += staticfiles_urlpatterns()
# Adding this allows us to locate the media/ folder in our project base location.
# This is import, as media/ contains all of the submitted files for a project.  
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
