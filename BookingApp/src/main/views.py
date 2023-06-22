import datetime
from django.shortcuts import render,reverse
from itertools import chain
from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse
from datetime import date, datetime, timedelta
from django.views import generic
from .models import *
# Create your views here.
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth import get_user_model
from django.utils import timezone
from .forms import LoginForm
from django.http import HttpResponse, JsonResponse
def index (request,room):

    all_rooms = Room.objects.all()
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
        date_to_filter = date.today() + timedelta(days=day-current_week_day)

    lectures = StudentLectureTeacher.objects.filter(room_number__exact=room).filter(date__exact=date_to_filter)
    bookings_teachers = TeacherBookingRoom.objects.filter(room_id__exact=room).filter(date__exact=date_to_filter)
    bookings_students = StudentBookingRoom.objects.filter(room_number__exact=room).filter(date__exact=date_to_filter)
    all_rooms = Room.objects.all()
    selected_room = Room.objects.get(room_number=room)
    context = {
        'day': day,
        'bookings_teachers': bookings_teachers,
        'bookings_students': bookings_students,
        'current_week_day': current_week_day,
        'room': room,
        'lectures': lectures,
        'all_rooms': all_rooms,
        'selected_room': selected_room,
    }
    return render(request=request , template_name= 'main/booking.html',context = context)

# def bookRoom(request, room, day):
#     if request.method == 'POST':
#         start_time = request.POST.get('startTime')
#         end_time = request.POST.get('endTime')
#         size = len(TeacherBookingRoom.objects.all())
#         bookingID = size+1
#         current_week_day = date.today().weekday()
#         date_to_filter = date.today() + timedelta(days=day-current_week_day)
#
#         # Parse the start and end time strings to datetime objects
#         start_time = datetime.strptime(start_time, '%H:%M').time()
#         end_time = datetime.strptime(end_time, '%H:%M').time()
#         print(start_time)
#
#         # Parse the current date
#         current_date = datetime.now().date()
#
#         # Combine the date and time components
#         start_datetime = datetime.combine(datetime.now().date(), start_time)
#         end_datetime = datetime.combine(datetime.now().date(), end_time)
#         duration = end_datetime - start_datetime
#
#         # Check if the booking duration exceeds the limit
#         max_duration = timedelta(hours=10)
#         if duration > max_duration:
#             error_message = "Booking duration exceeds the maximum limit of 10 hours."
#             return HttpResponse("duration error")
#
#         if request.user.is_authenticated:
#             user_id = request.user.id
#             teacherBook = Teacher.objects.filter(user=user_id)
#             studentBook = Student.objects.filter(user=user_id)
#
#
#             if teacherBook and not studentBook:
#
#                 overlapping_bookings = TeacherBookingRoom.objects.filter(
#                     room_id=room,
#                     time__lte=end_time,
#                     end_time__gte=start_time,
#                 )
#
#                 if overlapping_bookings.exists():
#                     error_message = "This room is already booked for the selected time period."
#                     return HttpResponse("time issue")
#                     # return render(request, 'main/booking.html', {'error_message': error_message})
#
#                 # overlapping_dates = TeacherBookingRoom.objects.filter(
#                 #     room_id=room,
#                 #     time__date=start_datetime.date(),
#                 #     end_time__date=end_datetime.date(),
#                 # )
#
#                 # if overlapping_dates.exists():
#                 #     error_message = "There is an overlapping booking for the selected date."
#                 #     return HttpResponse("date issue")
#                 #     # return render(request, 'main/booking.html', {'error_message': error_message})
#
#                 # booking = TeacherBookingRoom(booking_id=size + 1, time=start_time, end_time=end_time, date=day, room_number=room_number, teacher_id=1111)
#                 # booking.save()
#
#                 return HttpResponse("works")
#
#             elif studentBook and not teacherBook:
#                 return HttpResponse("Student")

def bookRoom(request, room, day):
    if request.method == 'POST':
        start_time = datetime.strptime(request.POST.get('startTime'), '%H:%M').time()
        end_time = datetime.strptime(request.POST.get('endTime'), '%H:%M').time()
        current_week_day = date.today().weekday()
        date_to_filter = date.today()
        roomObject = Room.objects.get(room_number=room)

        # Check duration limit - 10 hours
        duration_limit = timedelta(hours=10)
        booking_duration = datetime.combine(datetime.min.date(), end_time) - datetime.combine(datetime.min.date(),start_time)
        if booking_duration > duration_limit:
            # error_message = "Booking can not be more than 10 hours."
            # return render(request, 'main/booking.html', {'error_message': error_message})
            return HttpResponse("Duration issue")

        # if request.user.is_authenticated:
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
                    # return render(request, 'main/booking.html', {'error_message': error_message})
                    return HttpResponse("time issue")
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
                    # return render(request, 'main/booking.html', {'error_message': error_message})
                    return HttpResponse("time issue")

            # Save booking to database
            bookingS = StudentBookingRoom(booking_id=bookingIDS, student_number=student[0], room_number=roomObject, time=start_time, date=date_to_filter, end_time=end_time)
            bookingS.save()

        else:
            return HttpResponse("System error")

        # return HttpResponse("You are not authenticated")


    return HttpResponse("works")




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



