from django.contrib import admin
from django.urls import path,include
from account import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name='account' 

urlpatterns = [
    
    path('student/login/', views.student_login,name="student_login"),
    path('admin/login/', views.admin_login,name="admin_login"),
    path('student/register/', views.student_register.as_view(),name="student_register"),
    path('teacher/login/', views.teacher_login,name="teacher_login"),
    path('teacher/register/', views.teacher_register.as_view(),name="teacher_register"),
    path('change_password/student/$', views.change_password_stu,name="change_password_stu"),
    path('change_password/teacher/$', views.change_password_teach,name="change_password_teach"),

    path('password_reset/',auth_views.PasswordResetView.as_view(
            template_name='account/password/password_reset_form.html',
            email_template_name="account/password/password_reset_email.html",
            success_url=reverse_lazy('account:password_reset_done'),),
            name="reset_password"),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
            template_name='account/password/password_reset_done.html'), 
            name="password_reset_done"),

    path('password_reset/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(
            template_name='account/password/password_reset_confirm.html',
            success_url=reverse_lazy('account:password_reset_complete'),), 
            name='password_reset_confirm'),

    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(
            template_name='account/password/password_reset_complete.html'),
            name="password_reset_complete"),      

] 