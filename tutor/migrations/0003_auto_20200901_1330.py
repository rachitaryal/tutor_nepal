# Generated by Django 3.1 on 2020-09-01 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0002_tutorcoursegrade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorcoursegrade',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to='tutor.tutor'),
        ),
    ]