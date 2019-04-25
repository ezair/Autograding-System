# Generated by Django 2.2 on 2019-04-25 02:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='Assignment',
        ),
        migrations.AddField(
            model_name='assignment',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Project'),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='assigned_students',
            field=models.ManyToManyField(help_text='Assign students to assignment', to=settings.AUTH_USER_MODEL),
        ),
    ]
