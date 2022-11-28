from django.db import models
from account.models import Department,Subject,Teacher,Student
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
from datetime import datetime

class TimeTable(models.Model):
    time_id = models.IntegerField(primary_key=True)
    day = models.CharField(max_length = 20)
    start_time = models.CharField(max_length = 5)
    end_time = models.CharField(max_length = 5)
    sem = models.CharField(max_length = 5)
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)


class Student_attendance(models.Model):
    def to_time(value):   
        hhmm1 = value.split(' ')
        hhmm2 = str(hhmm1[1])
        hhmm = hhmm2[:5]
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        return hhmm

    attend_id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    attend_date = models.DateField(auto_now_add = True)
    attend_time = models.TimeField(default=datetime.now().strftime("%H:%M"))
    student = models.ForeignKey(Student,on_delete=models.CASCADE)


    def __str__(self):
        return str(self.subject)



