import datetime

from django.shortcuts import render,reverse
from django.http import HttpResponse
from datetime import date
from django.views import generic
from .models import *
# Create your views here.
from django.contrib.auth.views import LoginView as BaseLoginView
from .forms import LoginForm
def index (request):
    lectures = Lecture.objects.all()
    context = {
        "current_date" : date.today(),
        'lectures' : lectures
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
            return reverse('index')
        else:
            return reverse('login')
def BookingListView(request,room,day):
    current_week_day = date.today().weekday()
    date_to_filter = date.today()
    if (current_week_day<day):
        date_to_filter = date.today() + datetime.timedelta(days=day-current_week_day)
    lectures = StudentLectureTeacher.objects.filter(room_number__exact=room).filter(lecture_id__date__exact=date_to_filter)
    bookings_teachers = TeacherBookingRoom.objects.filter(room_id__exact=room).filter(date__exact = date_to_filter)
    bookings_students = StudentBookingRoom.objects.filter(room_number__exact=room).filter(date__exact = date_to_filter)
    all_bookings = lectures.union(bookings_students,bookings_teachers)
    all_rooms = Room.objects.all()

    context = {
        'all_bookings' : all_bookings,
        'current_week_day':current_week_day,
        'room':room,
        'all_rooms' : all_rooms
    }
    return render(request=request , template_name= 'main/booking.html',context = context)
