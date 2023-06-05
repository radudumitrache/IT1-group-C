from django.db import models


class Teacher(models.Model):
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


class StudentLectureTeacher(models.Model):
    lecture_id = models.ForeignKey("Lecture", null=False, on_delete=models.CASCADE)
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

