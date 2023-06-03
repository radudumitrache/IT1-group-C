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
