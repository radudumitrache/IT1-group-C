from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TeacherSerializer, TeacherBookingRoomSerializer, StudentSerializer, StudentBookingRoomSerializer, RoomSerializer, StudentLectureTeacherSerializer, LectureSerializer, ClassTypeSerializer
from main.models import Teacher, TeacherBookingRoom, Student, StudentBookingRoom, Room, StudentLectureTeacher, Lecture, ClassType


class TeacherListView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)


class TeacherBookingRoomListView(APIView):
    def get(self, request):
        teacher_bookings = TeacherBookingRoom.objects.all()
        serializer = TeacherBookingRoomSerializer(teacher_bookings, many=True)
        return Response(serializer.data)


class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class StudentBookingRoomListView(APIView):
    def get(self, request):
        student_bookings = StudentBookingRoom.objects.all()
        serializer = StudentBookingRoomSerializer(student_bookings, many=True)
        return Response(serializer.data)


class RoomListView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)


class StudentLectureTeacherListView(APIView):
    def get(self, request):
        student_lectures = StudentLectureTeacher.objects.all()
        serializer = StudentLectureTeacherSerializer(student_lectures, many=True)
        return Response(serializer.data)


class LectureListView(APIView):
    def get(self, request):
        lectures = Lecture.objects.all()
        serializer = LectureSerializer(lectures, many=True)
        return Response(serializer.data)


class ClassTypeListView(APIView):
    def get(self, request):
        class_types = ClassType.objects.all()
        serializer = ClassTypeSerializer(class_types, many=True)
        return Response(serializer.data)



'''
import json

from django.http import JsonResponse
from icalendar import Calendar
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_calendar(request, room):
    directory = os.path.join(os.path.dirname(__file__), 'calendar_files')
    file_name = f'{room}.ics'
    file_path = None

    for file in os.listdir(directory):
        if file.endswith('.ics') and room in file:
            file_path = os.path.join(directory, file)
            break

    if file_path is None:
        return JsonResponse({'error': f'Calendar file not found for room {room}'}, status=404)

    with open(file_path, 'rb') as calendar_file:
        cal = Calendar.from_ical(calendar_file.read())

    dictionary = {}

    def description_separation(summary: str):
        list_of_teachers = list()
        lecture_type = ""
        groups_present = list()
        lecture_type = summary.split(',')[0]
        summary = summary.replace(lecture_type, '')
        for element in summary.split(','):
            if ('-' in element and element.replace('-', '').isupper()):
                groups_present.append(element.strip())
                summary = summary.replace(element, '')

        list_of_teachers_unparsed = summary.split(',')
        list_of_teachers_unparsed = [x for x in list_of_teachers_unparsed if x != '']
        for i in range(0, len(list_of_teachers_unparsed)):
            if (i % 2 == 0):
                list_of_teachers.append(f"{list_of_teachers_unparsed[i]} {list_of_teachers_unparsed[i + 1]}".strip())
                continue

        return {"lecture type": lecture_type, "groups_present": groups_present, "list of teachers": list_of_teachers}

    id = 0
    for component in cal.walk():
        if (component.name == 'VEVENT'):
            start_time = str(component.decoded('dtstart')).split('+')[0]
            date = start_time.split()[0]
            start_time = start_time.split()[1]
            end_time = str(component.decoded('dtend')).split('+')[0]
            end_time = end_time.split()[1]
            description = description_separation(component.get('summary'))
            dictionary[f'{id}'] = {'name': component.get('name'), 'description': description,
                                   'location': component.get('location'), 'date': date, 'start': start_time,
                                   'end': end_time}
            id += 1
    json_data = json.dumps(dictionary)
    return Response(dictionary)
'''
