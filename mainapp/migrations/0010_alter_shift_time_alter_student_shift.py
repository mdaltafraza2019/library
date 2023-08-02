# Generated by Django 4.2 on 2023-07-27 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_alter_shift_time_alter_student_shift'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='time',
            field=models.CharField(blank=True, choices=[('7am_to_12pm', '7am_to_12pm'), ('12pm to 5pm', '12pm_to_5pm'), ('5pm_to 10pm', '5pm _o_10pm')], max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='shift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.shift'),
        ),
    ]
