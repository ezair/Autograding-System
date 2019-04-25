# Generated by Django 2.2 on 2019-04-25 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_at', models.DateField(auto_now_add=True)),
                ('files', models.FileField(help_text='Submit', null=True, upload_to='')),
                ('assignment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Assignment')),
            ],
        ),
    ]
