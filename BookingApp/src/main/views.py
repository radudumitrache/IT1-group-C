from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from django.views import generic
from .models import *
# Create your views here.

def index (request):
    lectures = Lecture.objects.all()
    context = {
        "current_date" : date.today(),
        'lectures' : lectures
    }
    return render(request = request , template_name = 'main/user_index.html',context = context)

def map(request):
    return render(request = request, template_name = 'main/map.html')
def login(request):
    return render(request = request, template_name = 'main/login.html')

def addRoom(request):
    return render(request = request, template_name = 'main/addRoom.html')

def listOfBookings(request):
    user_id = request.user.id
    teacherBookings = TeacherBookingRoom.objects.all()
    studentBookings = StudentBookingRoom.objects.all()

    bookings = teacherBookings.union(studentBookings)

    return render(request, 'main/listOfBookings.html', {'bookings' : bookings})

