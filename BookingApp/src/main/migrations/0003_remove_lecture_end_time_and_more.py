# Generated by Django 4.2.1 on 2023-06-05 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_lecture_end_time_studentbookingroom_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecture',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='studentbookingroom',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='teacherbookingroom',
            name='end_time',
        ),
    ]
