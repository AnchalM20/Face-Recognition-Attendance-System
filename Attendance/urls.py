from django.contrib import admin
from django.urls import path,include
from Attendance import views

app_name ="Attendance"

urlpatterns = [    
    path('training/', views.train_model,name="train_model"),
    path('testing/', views.test_model,name="test_model"),
    path("select_sub/",views.select_sub,name="select_sub"),
    path('dataset/',views.create_dataset,name="create_dataset"),
    path('attendance',views.attendance,name="attendance"),
    path('add_schedule',views.add_schedule,name="add_schedule")
]