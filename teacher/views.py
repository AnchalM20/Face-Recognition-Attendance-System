from django.shortcuts import render,redirect,HttpResponse
from account.views import student_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages,auth
from django.db import transaction
from django.contrib.auth.forms import UserChangeForm
from teacher.forms import ProfileUpdateForm, UserUpdateForm
from Attendance.models import Student_attendance, TimeTable
import xlwt
import datetime
from account.models import Teacher


def ttime_table(request):
    dept = request.user.teacher.department
    subject = request.user.teacher.subject
    m1 = TimeTable.objects.filter(department_id=dept, subject_id=subject)
    m2 = m1
    return render(request, 'teacher/ttime_table.html', {'m1': m1, 'm2': m2})
    
    
def teacher_dashboard(request):
    return render(request,'teacher/teacher_portal.html')

@login_required
def teacher_logout(request):
    auth.logout(request)
    return redirect('home')

@login_required
def teacher_profile(request):       
    if request.method == "POST":
        fm = UserUpdateForm(request.POST,instance=request.user)
        fm1 = ProfileUpdateForm(request.POST,
                                request.FILES,
                                instance=request.user.teacher)
        if fm.is_valid() and fm1.is_valid():
            fm.save()
            fm1.save()
            messages.success(request,f"Your profile has updated!!!")
            return redirect('teacher:teacher_profile')
    else:
        fm = UserUpdateForm(instance=request.user)
        fm1 = ProfileUpdateForm(instance=request.user.teacher)
        # return render(request,'student/student_profile.html',{'name':request.user,'name':request.user.student,'fm':fm, 'fm1':fm1})
    
    return render(request,'teacher/teacher_profile.html',{'fm':fm, 'fm1':fm1})
    
@login_required
def excel_report(request):
    teach_sub = request.user.teacher.subject
    
    if(teach_sub is None):
        messages.info(request,"You dont have any subject selected")
        return redirect('teacher:teacher_dashboard')
    else:
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename = Attendance-' + \
                    str(datetime.datetime.now())+'.xls'
        wb = xlwt.Workbook(encoding = 'utf-8')
        ws = wb.add_sheet('Attendance')
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ["Attendance Id","Subject","Attendance Date","Attendance Time",
                        "Student Name","Student Roll_no"]
        for col in range(len(columns)):
            ws.write(row_num,col,columns[col],font_style)

        rows = Student_attendance.objects.filter(subject = teach_sub)
        
        a = [x.attend_id for x in rows]
        b = [x.subject for x in rows]
        c = [x.attend_date for x in rows]
        d = [x.attend_time for x in rows]
        e = [x.student for x in rows]
        f = [x.student.roll_no for x in rows]
        data = [a,b,c,d,e,f]
        
        k=0
        for i in data:
            
            row_num = 0
            for j in range(len(i)):
                row_num += 1
                ws.write(row_num,k,str(i[j]),font_style)
            k += 1
        wb.save(response)

        return response
    
    
    