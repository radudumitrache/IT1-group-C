# Generated by Django 4.2.1 on 2023-06-05 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='end_time',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='studentbookingroom',
            name='end_time',
            field=models.TimeField(default=None),
        ),
        migrations.AddField(
            model_name='teacherbookingroom',
            name='end_time',
            field=models.TimeField(default=None),
        ),
    ]