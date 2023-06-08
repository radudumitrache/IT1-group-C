from rest_framework import serializers
from main.models import Teacher, TeacherBookingRoom, Student, StudentBookingRoom, Room, StudentLectureTeacher, Lecture, ClassType


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('teacher_number', 'first_name', 'last_name')


class TeacherBookingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherBookingRoom
        fields = ('booking_id', 'teacher_id', 'room_id', 'time', 'date')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('student_number', 'first_name', 'last_name')


class StudentBookingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentBookingRoom
        fields = ('booking_id', 'student_number', 'room_number', 'time', 'date')


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('room_number', 'availability')


class StudentLectureTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLectureTeacher
        fields = ('lecture_id', 'teacher_number', 'student_number', 'room_number')


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('lecture_id', 'lecture_type', 'lecture_name', 'date', 'time')


class ClassTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassType
        fields = ('lecture_type', 'description', 'colour')
