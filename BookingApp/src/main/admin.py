from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')

@admin.register(models.TeacherBookingRoom)
class TeacherBookingRoomAdmin(admin.ModelAdmin):
    list_display = ('booking_id','room_id','time','date','end_time')

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')

@admin.register(models.StudentBookingRoom)
class StudentBookingRoomAdmin(admin.ModelAdmin):
    list_display = ('booking_id','room_number','time','date','end_time')

@admin.register(models.StudentLectureTeacher)
class StudentLectureTeacherAdmin (admin.ModelAdmin):
    list_display = ('lecture_id','teacher_number','room_number','student_number','date','time','end_time')
@admin.register(models.Room)
class RoomAdmin (admin.ModelAdmin):
    list_display = ('room_number',)
@admin.register(models.Lecture)
class LectureAdmin (admin.ModelAdmin):
    list_display = ('lecture_id','lecture_type','lecture_name')
@admin.register(models.ClassType)
class ClassTypeAdmin (admin.ModelAdmin):
    list_display = ('lecture_type','description','colour')

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget = forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation',widget = forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ['email',]
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if (password1 and password2 and password1!=password2):
            raise ValidationError('Passwords do not match')
        return password2
    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if (commit):
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta :
        model = models.User
        fields = ['email','password','is_active','is_admin']

class UserAdmin (BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ['email','is_admin']
    list_filter = ['is_admin',]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),

        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2"],
            },
        ),
    ]
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = []

admin.site.register(models.User,UserAdmin)
admin.site.unregister(Group)
