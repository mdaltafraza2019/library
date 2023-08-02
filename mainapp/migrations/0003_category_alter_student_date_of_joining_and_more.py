# Generated by Django 4.2 on 2023-07-27 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_student_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(choices=[('Bpsc', 'Bpsc'), ('IIT', 'IIT'), ('NEET', 'NEET'), ('UPSC', 'UPSC'), ('JEE', 'JEE'), ('SSC', 'SSC'), ('Railway', 'Railway'), ('Banking', 'Banking')], max_length=30)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_joining',
            field=models.DateField(help_text='year-month-day'),
        ),
        migrations.AlterField(
            model_name='student',
            name='prep_for',
            field=models.CharField(choices=[('Bpsc', 'Bpsc'), ('IIT', 'IIT'), ('NEET', 'NEET'), ('UPSC', 'UPSC'), ('JEE', 'JEE'), ('SSC', 'SSC'), ('Railway', 'Railway'), ('Banking', 'Banking')], max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.category'),
        ),
    ]