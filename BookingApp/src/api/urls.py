from django.urls import path
from . import views

urlpatterns = [
    path('calendar/<str:week>/', views.get_calendar, name='get_calendar'),
]
