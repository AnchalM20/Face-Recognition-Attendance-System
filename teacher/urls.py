from django.contrib import admin
from django.urls import path,include
from teacher import views

app_name ="teacher"


urlpatterns = [

    path('profile/', views.teacher_profile,name="teacher_profile"),
    path('logout/', views.teacher_logout,name="teacher_logout"),
    path('excel/', views.excel_report,name="excel_report"),
    path('dashboard/', views.teacher_dashboard,name="teacher_dashboard"),
    path('time_table/',views.ttime_table,name="ttime_table"),

]