
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

class LoginForm (AuthenticationForm):
    email=forms.EmailInput()
    password = forms.PasswordInput()
from django import forms


class addRoomForm(forms.Form):
    roomName = forms.CharField(label="roomName", max_length=16, required=True)
    file = forms.FileField()
