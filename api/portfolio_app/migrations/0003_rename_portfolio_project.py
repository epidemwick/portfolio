# Generated by Django 4.2.2 on 2023-06-14 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_work_job_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Portfolio',
            new_name='Project',
        ),
    ]
