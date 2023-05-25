from django.urls import path
from . import views
app_name = 'ListOfBookings'
urlpatterns = [
    path("",views.index,name = 'index')
]