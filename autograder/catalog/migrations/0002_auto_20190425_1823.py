# Generated by Django 2.2 on 2019-04-25 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='crn',
            field=models.CharField(default='00000', help_text='Enter course title', max_length=6, unique=True),
        ),
    ]
