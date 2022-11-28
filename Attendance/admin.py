from django.contrib import admin
from Attendance.models import TimeTable,Student_attendance

class TimeTableAdmin(admin.ModelAdmin):
    search_fields = ['day','start_time','end_time',]
    list_filter = ['day','start_time','end_time',]
    list_display = ['day','start_time','end_time',]


class Student_attendanceAdmin(admin.ModelAdmin):
    search_fields = ['attend_id','status','attend_date',]
    list_filter = ['attend_id','status','attend_date',]
    list_display = ['attend_id','status','attend_date',]


admin.site.register(Student_attendance,Student_attendanceAdmin)
admin.site.register(TimeTable,TimeTableAdmin)