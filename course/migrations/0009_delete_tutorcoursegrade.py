# Generated by Django 3.1 on 2020-08-31 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20200831_1342'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TutorCourseGrade',
        ),
    ]
