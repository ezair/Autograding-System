from django.contrib import admin

from catalog.models import Project, TestCase, Assignment

admin.site.register(Assignment)
admin.site.register(Project)
admin.site.register(TestCase)
