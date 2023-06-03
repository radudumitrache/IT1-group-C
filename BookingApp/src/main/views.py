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

def index(request):
    lectures = Lecture.objects.all()
    context = {
        "current_date": date.today(),
        'lectures': lectures
    }
    return render(request=request, template_name='main/user_index.html', context=context)


def map(request):
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
