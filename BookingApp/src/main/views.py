from itertools import chain

from django.shortcuts import render, redirect
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


    # if bookingT:
    #     bookingT.delete()
    #     return redirect('listOfBookings')
    # elif not bookingT:
    #     bookingS = StudentBookingRoom.objects.get(booking_id=booking_id)
    #     if bookingS:
    #         bookingS.delete()
    #         return redirect('listOfBookings')
    #     else:
    #         return redirect('listOfBookings')

