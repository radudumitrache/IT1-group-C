from django import forms


class addRoomForm(forms.Form):
    roomName = forms.CharField(label="roomName", max_length=16, required=True)
    file = forms.FileField()