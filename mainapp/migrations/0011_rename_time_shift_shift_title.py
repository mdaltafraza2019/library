# Generated by Django 4.2 on 2023-07-27 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_shift_time_alter_student_shift'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shift',
            old_name='time',
            new_name='shift_title',
        ),
    ]
