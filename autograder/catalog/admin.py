from django.contrib import admin

from catalog.models import Project, TestCase, Assignment, Course

admin.site.register(Assignment)
admin.site.register(Project)
admin.site.register(TestCase)
admin.site.register(Course)
