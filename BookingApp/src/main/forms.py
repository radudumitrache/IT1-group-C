from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django import forms
from . import models
class LoginForm (AuthenticationForm):
    email=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    password = forms.PasswordInput(attrs={'placeholder': 'Enter your email'})

class MakeBookingForm (forms.ModelForm):
    chosenModel = None
    def __int__(self,request,*args,**kwargs):
        super(MakeBookingForm,self).__init__(*args,**kwargs)
        if (self.request.user.teacher):
            self.Meta.model = models.TeacherBookingRoom
        else :
            self.Meta.model = models.StudentBookingRoom
    class Meta():
        model = None
        fields =('startTime','endtime')
        widgets = {
            'startTime' : forms.TimeInput(attrs={'type' : 'time'}),
            'endTime': forms.TimeInput(attrs={'type': 'time'})
        }