from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserChangeForm
from django import forms
from account.models import User,Teacher,Student,Subject
from Attendance.models import TimeTable,Student_attendance
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.forms import ModelForm

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    password = None
    class Meta:
        model = User
        fields = ['username','email',]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name','last_name','roll_no','department','semester','image','contact_no']


class SelectSubForm(forms.ModelForm):
    class Meta:
        model = Student_attendance
        fields = ['subject']

    def __init__(self, user, *args, **kwargs):
        super(SelectSubForm, self).__init__(*args, **kwargs)
        self.fields['subject'].queryset = Subject.objects.filter(department_id = user.student.department,semester = user.student.semester)
       