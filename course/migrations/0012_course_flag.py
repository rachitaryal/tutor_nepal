# Generated by Django 3.1 on 2020-09-09 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_auto_20200901_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='flag',
            field=models.BooleanField(default=False),
        ),
    ]