from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
# Create your views here.
def index ( request):
    context = {
        "current_date" : date.today()
    }
    return render(request = request , template_name = 'main/user_index.html',context = context)