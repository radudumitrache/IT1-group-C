from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from django.views import generic
from .models import *
# Create your views here.
def index ( request):
    lectures = Lecture.objects.all()
    context = {
        "current_date" : date.today(),
        'lectures' : lectures
    }
    return render(request = request , template_name = 'main/user_index.html',context = context)