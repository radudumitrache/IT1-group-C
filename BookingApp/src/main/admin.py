from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')

@admin.register(models.TeacherBookingRoom)
class TeacherBookingRoomAdmin(admin.ModelAdmin):
    list_display = ('booking_id','room_id','time','date')

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')

@admin.register(models.StudentBookingRoom)
class StudentBookingRoomAdmin(admin.ModelAdmin):
    list_display = ('booking_id','room_number','time','date')

@admin.register(models.StudentLectureTeacher)
class StudentLectureTeacherAdmin (admin.ModelAdmin):
    list_display = ('lecture_id','teacher_number','room_number','student_number')
@admin.register(models.Room)
class RoomAdmin (admin.ModelAdmin):
    list_display = ('room_number',)
@admin.register(models.Lecture)
class LectureAdmin (admin.ModelAdmin):
    list_display = ('lecture_id','lecture_type','lecture_name','date','time')
@admin.register(models.ClassType)
class ClassTypeAdmin (admin.ModelAdmin):
    list_display = ('lecture_type','colour')