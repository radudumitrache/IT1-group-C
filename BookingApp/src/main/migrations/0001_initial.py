# Generated by Django 4.2.1 on 2023-06-04 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClassType',
            fields=[
                ('lecture_type', models.CharField(choices=[('ATELIER', 'Atelier'), ('WORKSHOP', 'Workshop'), ('TUTORIAL', 'Tutorial'), ('PLENARY', 'Plenary'), ('PERSONAL RESERVATION', 'Personal Reservation'), ('PROCESS', 'Process'), ('AVAILABLE', 'Available')], default='AVAILABLE', max_length=40, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('colour', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('lecture_id', models.IntegerField(primary_key=True, serialize=False)),
                ('lecture_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('lecture_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.classtype')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_number', models.IntegerField(primary_key=True, serialize=False)),
                ('availability', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_number', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_number', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherBookingRoom',
            fields=[
                ('booking_id', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='StudentLectureTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture', to='main.lecture')),
                ('room_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room')),
                ('student_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
                ('teacher_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='StudentBookingRoom',
            fields=[
                ('booking_id', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('room_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.room')),
                ('student_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
    ]
