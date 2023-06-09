import datetime
from django.shortcuts import render,reverse
from itertools import chain
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from datetime import date
from django.views import generic
from .models import *
# Create your views here.
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth import get_user_model
from .forms import LoginForm
def index (request,room):

    all_rooms = Room.objects.all()
    # lectures = StudentLectureTeacher.objects.filter(room_number__exact=room).filter(
    #     lecture_id__date__exact=datetime.date.today())
    # bookings_teachers = TeacherBookingRoom.objects.filter(room_id__exact=room).filter(date__exact=datetime.date.today())
    # bookings_students = StudentBookingRoom.objects.filter(room_number__exact=room).filter(date__exact=datetime.date.today())
    lectures = StudentLectureTeacher.objects.all()
    bookings_teachers = TeacherBookingRoom.objects.all()
    bookings_students = StudentBookingRoom.objects.all()
    all_bookings = lectures.union(bookings_students, bookings_teachers)


    context = {
        'all_rooms' : all_rooms,
        "current_date" : date.today(),
        'all_booking' : all_bookings
    }
    return render(request = request , template_name = 'main/user_index.html',context = context)

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
        date_to_filter = date.today() + datetime.timedelta(days=day-current_week_day)
    lectures = StudentLectureTeacher.objects.filter(room_number__exact=room).filter(date__exact=date_to_filter)
    lectures = lectures.select_related('lecture_id').values('lecture_id__lecture_type')
    bookings_teachers = TeacherBookingRoom.objects.filter(room_id__exact=room).filter(date__exact = date_to_filter)
    bookings_students = StudentBookingRoom.objects.filter(room_number__exact=room).filter(date__exact = date_to_filter)
    bookings_students = list ( bookings_students.values())
    bookings_teachers = list ( bookings_teachers.values())
    lectures = list ( lectures.values())
    all_bookings = bookings_teachers + bookings_students + lectures
    all_rooms = Room.objects.all()
    context = {
        'all_bookings' : all_bookings,
        'current_week_day':current_week_day,
        'room':room,
        'lectures' : lectures,
        'all_rooms' : all_rooms
    }
    return render(request=request , template_name= 'main/booking.html',context = context)
def listOfBookings(request):
    user = request.user.id
    bookings = None
    if (Student.objects.filter(user__exact=user).exists()):
        bookings = Student.objects.filter(user__exact=user)
    elif (Teacher.objects.filter(user__exact=user).exists()):
        bookings = Teacher.objects.filter(user__exact=user)
    return render(request, 'main/listOfBookings.html', {'bookings' : bookings})

def deleteBooking(request, booking_id):
    bookingT = TeacherBookingRoom.objects.filter(booking_id=booking_id)
    bookingS = StudentBookingRoom.objects.filter(booking_id=booking_id)
    # user_id = request.user.id
    if bookingT and not bookingS:
        # bookingT = TeacherBookingRoom.objects.get(booking_id=booking_id)
        # teacherBookings = bookingT.objects.filter(teacher_id=user_id)
        bookingT.delete()
        return  redirect('listOfBookings')
    elif bookingS and not bookingT:
        # bookingS = StudentBookingRoom.objects.get(booking_id=booking_id)
        # studentBookings = bookingS.objects.filter(student_number=user_id)
        bookingS.delete()
        return redirect('listOfBookings')
    else:
        return redirect('listOfBookings')



