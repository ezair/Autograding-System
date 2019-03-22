from django.db import models
from django.contrib.auth.models import Group, User


class Assignment(models.Model):
    name = models.CharField(max_length=60, help_text='Enter a name')

    due_date = models.DateField(null=True, blank=True)

    assigned_students = models.ManyToManyField(User, help_text='Assign students to assignmnet')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this assignmnet."""
        return reverse('assignmnet-detail', args=[str(self.id)])


class Project(models.Model):
    short_description = models.CharField(max_length=60, help_text='Enter a short description')

    long_description = models.TextField(help_text='Enter a detailed description')

    Assignment = models.ForeignKey('Assignment', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.short_description

class TestCase(models.Model):
    name = models.CharField(max_length=60, help_text='Enter a name')

    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
