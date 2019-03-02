from django.urls import path
from . import views

# Stick to the nameing conventions for the name= parameter.
# it is always 'app_name-html_file_name' and nothing else.
urlpatterns = [
    path('', views.index, name='catalog_index'),
]
