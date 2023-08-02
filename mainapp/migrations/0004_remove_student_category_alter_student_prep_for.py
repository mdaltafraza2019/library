# Generated by Django 4.2 on 2023-07-27 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_category_alter_student_date_of_joining_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='category',
        ),
        migrations.AlterField(
            model_name='student',
            name='prep_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.category'),
        ),
    ]