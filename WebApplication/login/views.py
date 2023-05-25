from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def login_page (request):
    return render(request = request, template_name= 'login.html')