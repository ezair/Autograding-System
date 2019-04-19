# Generated by Django 2.1.7 on 2019-04-18 23:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20190417_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite',
            name='group_choice',
            field=models.CharField(choices=[('Instructor', 'INSTRUCTOR'), ('Student', 'STUDENT'), ('Grader', 'GRADER')], default=('Student', 'STUDENT'), max_length=20),
        ),
        migrations.AlterField(
            model_name='invite',
            name='invite_sender',
            field=models.ForeignKey(default='autograderinstructor', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='invite_sender', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]