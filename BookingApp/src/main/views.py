from itertools import chain
from django.shortcuts import render, redirect,reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from django.views import generic
from .models import *
from django.http import HttpResponseRedirect
from .forms import addRoomForm
from helperfunctions import handle_uploaded_file


# Create your views here.
from django.contrib.auth.views import LoginView as BaseLoginView
from .forms import LoginForm

def index(request):
    lectures = Lecture.objects.all()
    context = {
        "current_date": date.today(),
        'lectures': lectures
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
            return reverse('index')
        else:
            return reverse('login')
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

    return render(request=request, template_name='main/map.html')


def login(request):
    return render(request=request, template_name='main/login.html')


def addRoom(request):
    return render(request=request, template_name='main/addRoom.html')


def get_room(request):
    if request.method == "POST":
        form = addRoomForm(request.POST, request.FILES["file"])
        if form.is_valid():
            if form.cleaned_data["roomName"] == "K 5.01 - IOT Lab" or form.cleaned_data["roomName"] == "K 5.01":
                roomName = form.cleaned_data["roomName"]
                file = request.FILES['file']
                handle_uploaded_file(file)
                return HttpResponseRedirect("/addRoom")
            elif (form.cleaned_data["roomName"].find('.') == 1) and (form.cleaned_data["roomName"].count(".") == 1):
                roomName = form.cleaned_data["roomName"]
                file = request.FILES['file']
                handle_uploaded_file(file)
                return HttpResponseRedirect("/addRoom")
            else:
                raise ValidationError(
                    _("Invalid value: %(value)s"),
                    code="invalid",
                    params={"value": form.cleaned_data["roomName"]}
                )
        else:
            form = addRoomForm()
            return render(request, "addRoom.html", {"form": form})
