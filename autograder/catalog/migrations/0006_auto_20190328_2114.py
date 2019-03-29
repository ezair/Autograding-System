# Generated by Django 2.1.7 on 2019-03-29 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_course_name1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='name1',
        ),
        migrations.AddField(
            model_name='course',
            name='crn',
            field=models.CharField(default='00000', help_text='Enter course title', max_length=6),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default='This class description', help_text='Enter a detailed description'),
        ),
    ]
