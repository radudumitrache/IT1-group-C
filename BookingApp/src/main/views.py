import datetime
from itertools import chain
from django.shortcuts import render, redirect,reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date, datetime, timedelta
from django.views import generic
from .models import *
from django.http import HttpResponseRedirect
from .parser import calendar_parse
import django
import json
from .models import StudentLectureTeacher, Lecture
import os


# Create your views here.
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth import get_user_model
from .forms import LoginForm
from .forms import addRoomForm


from django.http import HttpResponse
def index (request,room):
    date_to_filter = date.today()
    all_rooms = Room.objects.all()
    lectures = StudentLectureTeacher.objects.filter(room_number__exact=room).filter(date__exact=date_to_filter)
    bookings_teachers = TeacherBookingRoom.objects.filter(room_id__exact=room).filter(date__exact=date_to_filter)
    bookings_students = StudentBookingRoom.objects.filter(room_number__exact=room).filter(date__exact=date_to_filter)
    all_rooms = Room.objects.all()
    context = {
        'bookings_teachers': bookings_teachers,
        'bookings_students': bookings_students,
        'room': room,
        'lectures': lectures,
        'all_rooms': all_rooms,
    }
    return render(request=request, template_name='main/user_index.html', context=context)


def map(request):
    return render(request = request, template_name = 'main/map.html')

def addRoom(request):
    return render(request = request, template_name = 'main/addRoom.html')
class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = 'main/login.html'
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    def get_success_url(self):
        user =self.request.user
        if (user.is_authenticated):
            return reverse('index',args=[str(1)])
        else:
            return reverse('login')
def BookingListView(request,room,day):
    current_week_day = date.today().weekday()
    date_to_filter = date.today()
    if (current_week_day<day):
        date_to_filter = date.today() + timedelta(days=day-current_week_day)

    lectures = StudentLectureTeacher.objects.filter(room_number__exact=room).filter(date__exact=date_to_filter)
    bookings_teachers = TeacherBookingRoom.objects.filter(room_id__exact=room).filter(date__exact=date_to_filter)
    bookings_students = StudentBookingRoom.objects.filter(room_number__exact=room).filter(date__exact=date_to_filter)
    all_rooms = Room.objects.all()
    context = {
        'day': day,
        'bookings_teachers': bookings_teachers,
        'bookings_students': bookings_students,
        'current_week_day': current_week_day,
        'room': room,
        'lectures': lectures,
        'all_rooms': all_rooms,
    }
    return render(request=request , template_name= 'main/booking.html',context = context)

def bookRoom(request, room, day):
    if request.method == 'POST':
        start_time = datetime.strptime(request.POST.get('startTime'), '%H:%M').time()
        end_time = datetime.strptime(request.POST.get('endTime'), '%H:%M').time()
        current_week_day = date.today().weekday()
        date_to_filter = date.today()
        if (current_week_day < day):
            date_to_filter = date.today() + timedelta(days=day - current_week_day)

        roomObject = Room.objects.get(room_number=room)

        # Check duration limit - 10 hours
        duration_limit = timedelta(hours=10)
        booking_duration = datetime.combine(datetime.min.date(), end_time) - datetime.combine(datetime.min.date(),start_time)
        if booking_duration > duration_limit:

            # error_message = "Booking can not be more than 10 hours."
            # return render(request, 'main/listOfBookings.html')
            # return HttpResponse("Duration issue")
            return redirect('listOfBookings')


        user_id = request.user.id

        student = Student.objects.filter(user_id=user_id)
        teacher = Teacher.objects.filter(user_id=user_id)

        if teacher and not student:

            sizeT = len(TeacherBookingRoom.objects.all())
            bookingIDT = sizeT + 1

            # Check for overlapping bookings
            bookingsT = TeacherBookingRoom.objects.filter(date=date_to_filter, room_id=room)
            for booking in bookingsT:
                if start_time < booking.end_time and end_time > booking.time:
                    # error_message = "This room is already booked for this time."
                    # return render(request, 'main/listOfBookings.html')
                    # return HttpResponse("time issue")
                    return redirect('listOfBookings')
            # Save booking to database
            bookingT = TeacherBookingRoom(booking_id=bookingIDT, teacher_id=teacher[0], room_id=roomObject, time=start_time, end_time=end_time,date=date_to_filter)
            bookingT.save()

        elif student and not teacher:

            sizeS = len(StudentBookingRoom.objects.all())
            bookingIDS = sizeS + 1

            # Check for overlapping bookings
            bookingsS = StudentBookingRoom.objects.filter(date=date_to_filter, room_number=room)
            for booking in bookingsS:
                if start_time < booking.end_time and end_time > booking.time:
                    # error_message = "This room is already booked for this time."
                    # return render(request, 'main/listOfBookings.html')
                    return redirect('listOfBookings')
                    # return HttpResponse("time issue")

            # Save booking to database
            bookingS = StudentBookingRoom(booking_id=bookingIDS, student_number=student[0], room_number=roomObject, time=start_time, date=date_to_filter, end_time=end_time)
            bookingS.save()

        else:
            return HttpResponse("System error")


    # successMessage = "Your booking has been successful!"
    # return render(request, 'main/listOfBookings.html')
    return redirect('listOfBookings')
    # return redirect('listOfBookings', {'success_message':success_message})
    # return HttpResponse("works")

def listOfBookings(request):
    user = request.user.id

    bookings = None
    if (Student.objects.filter(user__exact=user).exists()):
        student_number = Student.objects.get(user=user).student_number
        bookings = StudentBookingRoom.objects.filter(student_number=student_number)
    elif (Teacher.objects.filter(user__exact=user).exists()):
        teacher_id = Teacher.objects.get(user=user).teacher_number
        bookings = TeacherBookingRoom.objects.filter(teacher_id=teacher_id)
    return render(request, 'main/listOfBookings.html', {'bookings' : bookings})

def deleteBooking(request, booking_id):
    bookingT = TeacherBookingRoom.objects.filter(booking_id=booking_id)
    bookingS = StudentBookingRoom.objects.filter(booking_id=booking_id)
    if bookingT and not bookingS:
        bookingT.delete()
        return  redirect('listOfBookings')
    elif bookingS and not bookingT:
        bookingS.delete()
        return redirect('listOfBookings')
    else:
        return redirect('listOfBookings')

    return render(request=request, template_name='main/map.html')

def login(request):
    return render(request=request, template_name='main/login.html')


def addRoom(request):
    if request.method == 'POST':
        calendar_parse()
        insert_json_data_Teacherdata()
        insert_json_data_RoomNumberdata()
        insert_json_data_LectureNamedata()
        insert_json_data_Datedata()
        insert_json_data_Timedata()
        insert_json_data_LectureTypedata()
        return render(request=request, template_name='main/addRoom.html')
    else:
        return render(request=request, template_name='main/addRoom.html')

def add_lecture (dict):
    for key,lecture in dict:
        pass

def get_room(request):
    form = None
    if request.method == "POST":
        form = addRoomForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data["roomName"] == "K 5.01 - IOT Lab" or form.cleaned_data["roomName"] == "K 5.01":
                roomName = form.cleaned_data["roomName"]
                file = form.cleaned_data['file']
                file_path = 'icsFiles/schedule.ics'
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path,'wb') as destination :
                    for line in file.readlines():
                        destination.write(line)
                calendar_file = open(file_path,'rb')
                result_dictionary = calendar_parse(calendar_file)
                return HttpResponseRedirect("/addRoom")
            elif (form.cleaned_data["roomName"].find('.') == 1) and (form.cleaned_data["roomName"].count(".") == 1):
                roomName = form.cleaned_data["roomName"]
                file = form.cleaned_data['file']
                file_path = 'icsFiles/schedule.ics'
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, 'wb') as destination:
                    for line in file.readlines():
                        destination.write(line)
                calendar_file = open(file_path,'rb')
                result_dictionary = calendar_parse(calendar_file)
                return HttpResponseRedirect("/addRoom")
            else:
                raise ValidationError(
                    _("Invalid value: %(value)s"),
                    code="invalid",
                    params={"value": form.cleaned_data["roomName"]}
                )
        else:
            form = addRoomForm()
    return render(request, "main/addRoom.html", {"form": form})


def insert_json_data_Teacherdata():
    parsed_data = json.load()
    for item in parsed_data:
        studentModel = StudentLectureTeacher(json_data=item)
        studentModel.save()
def insert_json_data_RoomNumberdata():
    parsed_data = json.load()
    for item in parsed_data:
        studentModel = StudentLectureTeacher(json_data=item)
        studentModel.save()


def insert_json_data_LectureNamedata():
    parsed_data = json.load()
    for item in parsed_data:
        lectureModel = Lecture(json_data=item)
        lectureModel.save()

def insert_json_data_Datedata():
    parsed_data = json.load()
    for item in parsed_data:
        lectureModel = Lecture(json_data=item)
        lectureModel.save()

def insert_json_data_Timedata():
    parsed_data = json.load()
    for item in parsed_data:
        lectureModel = Lecture(json_data=item)
        lectureModel.save()

def insert_json_data_LectureTypedata():
    parsed_data = json.load()
    for item in parsed_data:
        lectureModel = Lecture(json_data=item)
        lectureModel.save()