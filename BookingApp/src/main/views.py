from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index ( request):
    return HttpResponse("hello world")

def addRoom(request):
    return render(request = request, template_name = 'main/addRoom.html')