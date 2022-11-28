from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.db import transaction
from django.contrib.auth.forms import UserChangeForm
from student.forms import ProfileUpdateForm, UserUpdateForm
from Attendance.models import TimeTable, Student_attendance
from account.models import Department
from django.db.models import Count
from django.core.mail import send_mail
import datetime
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import pandas as pd
import numpy as np


@login_required
def time_table(request):
    dept = request.user.student.department
    sem = request.user.student.semester
    m1 = TimeTable.objects.filter(department_id=dept, sem=sem)
    m2 = m1
    return render(request, 'student/time_table.html', {'m1': m1, 'm2': m2})


@login_required
def student_dashboard(request):
    return render(request, 'student/student_portal.html')


@login_required
def student_profile(request):
    if request.method == "POST":
        fm = UserUpdateForm(request.POST, instance=request.user)
        fm1 = ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.student)
        if fm.is_valid() and fm1.is_valid():
            fm.save()
            fm1.save()
            messages.success(request, f"Your profile has updated!!!")
            return redirect('student:student_profile')
    else:
        fm = UserUpdateForm(instance=request.user)
        fm1 = ProfileUpdateForm(instance=request.user.student)

    return render(request, 'student/student_profile.html', {'fm': fm, 'fm1': fm1})


@login_required
def student_logout(request):
    auth.logout(request)
    return redirect('home')


@login_required
def training_webcam(request):
    return render(request, 'Attendance/training_webcam.html')


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, formate='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x,y,a,b):
    plt.switch_backend("AGG")
    plt.title("Per day subject attended",fontsize = 16)    
    plt.plot(x,y,label="week1")
    plt.plot(a,b,label="week2")
    plt.xlabel("Week day ",fontsize = 14)
    plt.ylabel("Lecture attended per week",fontsize = 14)
    plt.legend()    
    graph = get_graph()
    return graph
    
def get_pie(x):
    plt.switch_backend("AGG")
    plt.title("Week wise present absent",fontsize = 20)
    colors = ["green","red"]
    labels="Present","Absent"
    plt.pie([x,15-x],explode=(0, 0.1), labels=labels,
                autopct='%1.1f%%', shadow=True, startangle=90,textprops={'fontsize': 16},colors=colors)
    graph = get_graph()
    return graph

def get_bar(x,y,a,b1):
    b = []
    for (i,k) in zip(a,b1):
        for j in x:
            if(j == i):
                b.append(k)
                break
    
    plt.figure(figsize=(100,100))
    plt.switch_backend("AGG")  
    
    X_axis1 = np.arange(len(x))
    plot = plt.bar(X_axis1 - 0.2, y, 0.4, label = 'Week1')
    plt.xticks(X_axis1, x, rotation=45)    
    
    X_axis2 = np.arange(len(a))
    plt.bar(X_axis2 + 0.2, b, 0.4, label = 'Week2')
        
    plt.title("Attendance of last week in %",fontsize = 16)
    plt.xlabel("Subjects",fontsize = 14)
    plt.ylabel("Percentage(%) of attendance",fontsize = 14)
    plt.legend()
    plt.tight_layout()
    graph = get_graph()
    return graph


@login_required
def attendance_report(request):
    stu = request.user.student
    attend_data = Student_attendance.objects.filter(student = stu)
    
    a = [x.subject for x in attend_data]
    b = [x.attend_date for x in attend_data]
    c = [x.attend_time for x in attend_data]
    d = [x.status for x in attend_data]
    
    dictionary = {
        "Subject": a,
        "Attend_date": b,
        "Attend_time": c,
        "Status": d,
    }
    df = pd.DataFrame(dictionary)
    
    df["Attend_date"] = pd.to_datetime(df["Attend_date"], errors='coerce')
    df["Day"] = df["Attend_date"].dt.day_name()
    df["Week"] = df["Attend_date"].dt.week
    df["Status"] = df["Status"].astype(int)
    df["Subject"] = df["Subject"].astype(str)
    lecture = [3,3,3,2,4]
    week_group = df.groupby(df["Week"])
    
    g1 = week_group.get_group(17)

    g2 = week_group.get_group(18)
    
    g1["day_sum"] = g1.groupby("Day")["Status"].transform('sum')
    #week1_day_attend = get_plot(g1["Day"],g1["day_sum"]) 
        
    g1["sub_sum"] = g1.groupby("Subject")["Status"].transform('sum')
    g = g1[["Subject","sub_sum"]].drop_duplicates()
    g["total_lec"] = lecture
    
    g2["day_sum"] = g2.groupby("Day")["Status"].transform('sum')
    #week2_day_attend = get_plot(g2["Day"],g2["day_sum"])     
    
    g2["sub_sum"] = g2.groupby("Subject")["Status"].transform('sum')
    g3 = g2[["Subject","sub_sum"]].drop_duplicates()
   
    count = 0
    lec = []
    for l in lecture:
        lec.append(l)
        count += 1
        if(count > len(g3["sub_sum"])):
            break
    
    sum1 = g["sub_sum"].sum()
    sum2 = g3["sub_sum"].sum()
    
    if(((sum1+sum2)/2<15) and datetime.datetime.now().hour < 12):
        
        perc = ((sum1+sum2)/2)*(100/15)
        send_mail(f"Alert! Low Attendace",f"Good Afternoon {request.user.student.first_name} {request.user.student.last_name} This is to notify you that your attendance is only {perc}% which is very low. Please be on time for next lecture."
                ,"anchallsm2000@gmail.com",[request.user.email],fail_silently = False)
        
    week_day_attend = get_plot(g1["Day"],g1["day_sum"],g2["Day"],g2["day_sum"])
    week_sub_attend = get_bar(g["Subject"],[(j/i)*100 for (i,j) in zip(g["total_lec"],g["sub_sum"])],g3["Subject"],[(j/i)*100 for (i,j) in zip(lecture,g3["sub_sum"])])
    
    return render(request, 'student/report.html', {"a": attend_data, "b": week_day_attend,"c": week_sub_attend,"d":get_pie(sum1),"e":get_pie(sum2)})
