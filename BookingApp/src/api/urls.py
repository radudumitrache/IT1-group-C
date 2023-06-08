from django.urls import path
from .views import (
    TeacherListView, TeacherBookingRoomListView, StudentListView, StudentBookingRoomListView,
    RoomListView, StudentLectureTeacherListView, LectureListView, ClassTypeListView
)

urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('teacher-bookings/', TeacherBookingRoomListView.as_view(), name='teacher-booking-list'),
    path('students/', StudentListView.as_view(), name='student-list'),
    path('student-bookings/', StudentBookingRoomListView.as_view(), name='student-booking-list'),
    path('rooms/', RoomListView.as_view(), name='room-list'),
    path('student-lectures/', StudentLectureTeacherListView.as_view(), name='student-lecture-list'),
    path('lectures/', LectureListView.as_view(), name='lecture-list'),
    path('lecture-types/', ClassTypeListView.as_view(), name='lecture-type-list'),
]
