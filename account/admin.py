from django.contrib import admin
from account.models import Student,Teacher,User,Department,Subject

class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ["department_id","department_name",]
    list_filter = ["department_id",]
    list_display = ["department_id","department_name",]

class SubjectAdmin(admin.ModelAdmin):
    search_fields = ["subject_id","subject_name",]
    list_filter = ["subject_name",]
    list_display = ["subject_id","subject_name",]

class UserAdmin(admin.ModelAdmin):
    search_fields = ["username","email",]
    list_filter = ["username",]
    list_display = ["pk",'email','username',]

class StudentAdmin(admin.ModelAdmin):
    search_fields = ["first_name","roll_no",'semester']
    list_filter = ["roll_no"]
    list_display = ['first_name','roll_no','department','semester',]

class TeacherAdmin(admin.ModelAdmin):
    search_fields = ["first_name","department",]
    list_filter = ['first_name',]
    list_display = ['first_name','department',]


admin.site.register(User,UserAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)