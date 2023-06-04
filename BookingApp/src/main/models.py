from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.urls import reverse
class UserManager(BaseUserManager):
    def create_user(self,email,password = None):
        if not email :
            raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email),

        )
        user.set_password(password)
        user.save(using = self.db)
        return user
    def create_superuser(self,email,password = None):
        user = self.create_user(email,password)
        user.is_admin = True
        user.save(using=self.db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj = None):
        return True
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin


class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    teacher_number = models.CharField(max_length=30, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class TeacherBookingRoom(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    teacher_id = models.ForeignKey("Teacher", null=False, on_delete=models.CASCADE)
    room_id = models.ForeignKey("Room", null=False, on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField()

    def date_now(self):
        return self.date.strftime("%Y-%m-%d")

    def time_now(self):
        return self.time.strftime("%H:%M")



class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    student_number = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __str__(self):
        return str(self.student_number)


class StudentBookingRoom(models.Model):
    booking_id = models.IntegerField(primary_key=True)
    student_number = models.ForeignKey("Student", null=False, on_delete=models.CASCADE)
    room_number = models.ForeignKey("Room", null=False, on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField()

    def date_now(self):
        return self.date.strftime("%Y-%m-%d")

    def time_now(self):
        return self.time.strftime("%H:%M")

class Room(models.Model):
    room_number = models.IntegerField(primary_key=True)
    availability = models.BooleanField()
    def __str__(self):
        return str(self.room_number)


class StudentLectureTeacher(models.Model):
    lecture_id = models.ForeignKey("Lecture", null=False, on_delete=models.CASCADE , related_name= 'lecture')
    teacher_number = models.ForeignKey("Teacher", null=False, on_delete=models.CASCADE)
    student_number = models.ForeignKey("Student", null=False, on_delete=models.CASCADE)
    room_number = models.ForeignKey("Room", null=False, on_delete=models.CASCADE)





class Lecture(models.Model):
    lecture_id = models.IntegerField(primary_key=True)
    lecture_type = models.ForeignKey("ClassType", null=False, on_delete=models.CASCADE)
    lecture_name = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()

    def date_now(self):
        return self.date.strftime("%Y-%m-%d")

    def time_now(self):
        return self.time.strftime("%H:%M")

class ClassType(models.Model):
    ATLR = "ATELIER"
    WRKSHP = "WORKSHOP"
    TTRL = "TUTORIAL"
    PLNR = "PLENARY"
    PRSNL_RES = "PERSONAL RESERVATION"
    PRCSS = "PROCESS"
    AVLBL = "AVAILABLE"
    DIFFERENT_LECTURE_TYPES = [
        (ATLR, "Atelier"),
        (WRKSHP, "Workshop"),
        (TTRL, "Tutorial"),
        (PLNR, "Plenary"),
        (PRSNL_RES, "Personal Reservation"),
        (PRCSS, "Process"),
        (AVLBL, "Available")
    ]
    lecture_type = models.CharField(primary_key=True, max_length=40, choices=DIFFERENT_LECTURE_TYPES, default=AVLBL)
    description = models.TextField()
    colour = models.CharField(max_length=20)