from django.shortcuts import render,redirect,reverse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from account.forms import StudentSignUpForm,TeacherSignUpForm
from account.models import User,Teacher,Student
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from student.views import student_dashboard
    
@login_required
def change_password_stu(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password is successfully updated!')
            return redirect('student:student_dashboard')
        else:
            messages.error(request, 'Please enter valid password(include num,symbol and char')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {'form': form})
    
def change_password_teach(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password is successfully updated!')
            return redirect('account:change_password_teach')
        else:
            messages.error(request, 'Please enter valid password(include num,symbol and char')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password1.html', {'form': form})

def admin_login(request):
    if request.method =="POST":
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('Attendance:attendance')
            else:
                messages.error(request,"Username does not exist")
                return render(request,'account/admin_login.html',{'form':form})
        else:
            messages.error(request,"username or password is incorrect!!")
            return render(request,'account/admin_login.html',{'form':form})
                
    else:
        form = AuthenticationForm()
        return render(request,'account/admin_login.html',{'form':form})

#Student
def student_login(request):
    if request.method =="POST":
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('student:student_dashboard')
            # else:
            #     messages.error(request,"username or password is incorrect!!")
            #     return render(request,'account/student_login.html',{'form':form})
        else:
            messages.error(request,"username or password is incorrect!!")
            return render(request,'account/student_login.html',{'form':form})
                
    else:
        form = AuthenticationForm()
        return render(request,'account/student_login.html',{'form':form})

class student_register(CreateView):
    form_class = StudentSignUpForm
    model = User
    template_name = 'account/student_register.html'

    def get_success_url(self):
        return reverse('account:student_login')

#Teacher
def teacher_login(request):
    if request.method =="POST":
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('teacher:teacher_dashboard')
            # else:
            #     messages.error(request,"username or password is incorrect!!")
            #     return render(request,'account/student_login.html',{'form':form})
        else:
            messages.error(request,"username or password is incorrect!!")
            return render(request,'account/teacher_login.html',{'form':form})
                
    else:
        form = AuthenticationForm()
        return render(request,'account/teacher_login.html',{'form':form})

class teacher_register(CreateView):
    form_class = TeacherSignUpForm
    model = User
    template_name = 'account/teacher_register.html'

    def get_success_url(self):
        return reverse('account:teacher_login')


