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
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
'''
Description:
Last edited by: Eric Zair
Last edited on: 02/26/2019
'''


# Simply contains the paths to different applications in our project.
# This list of urls will ONLY have paths to default apps and to our homepage.
# NOTE:	Path to homepage should be '/'.
#	EVEN MORE IMPORTANT NOTE:
#		When it comes to using the "name=" parameter, always name the link
#		name='application_name-the_name_of_the_template'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls'), name='accounts'),
]

from django.urls import include
from django.urls import path

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# So that we can load static files properly from ALL url locations.
# This DOES NOT need to be added to any other urls.py files.
urlpatterns += staticfiles_urlpatterns()
