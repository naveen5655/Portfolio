# Generated by Django 4.0.3 on 2022-03-17 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_student_customer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Student',
        ),
    ]
