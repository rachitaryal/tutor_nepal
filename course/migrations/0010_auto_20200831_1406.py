# Generated by Django 3.1 on 2020-08-31 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_delete_tutorcoursegrade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
