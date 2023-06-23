"""
URL configuration for BookingSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import RedirectView
from . import views
urlpatterns = [
    path("index/<str:room>",views.index,name = 'index'),
    path('map/',views.map,name = 'map'),
    path('login/',views.LoginView.as_view(),name = 'login'),
    path('addRoom/', views.get_room, name='addRoom'),
    path('booking/<str:room>/<int:day>/', views.BookingListView,name = 'booking'),
    path('bookRoom/<str:room>/<int:day>/', views.bookRoom,name = 'bookRoom'),
    path('listOfBookings/', views.listOfBookings, name = 'listOfBookings'),
    path('listOfBookings/<int:booking_id>/cancel', views.deleteBooking, name = 'cancelBooking')
]

