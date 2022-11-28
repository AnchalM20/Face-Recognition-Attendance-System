from django.contrib import admin
from django.urls import path,include
from . import views
from Attendance.views import select_sub

app_name ="student"

urlpatterns = [

    path('profile/', views.student_profile,name="student_profile"),
    path('logout/', views.student_logout,name="student_logout"),
    path('dashboard/', views.student_dashboard,name="student_dashboard"),
    path('time_table/',views.time_table,name="time_table"),
    path('report/',views.attendance_report,name="attendance_report"),
  
]