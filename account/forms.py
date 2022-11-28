from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User,Teacher,Student,Department
from django.db import transaction
from django.forms import ModelChoiceField


class StudentSignUpForm(UserCreationForm):
        first_name = forms.CharField(max_length=50)
        last_name = forms.CharField(max_length=50)
        email = forms.EmailField(max_length = 100)
        #     roll_no = forms.CharField(max_length=10)
        #     semester_no = forms.CharField(max_length=10)
        department = forms.ModelChoiceField(queryset = Department.objects.all(),required = True)
        contact_no = forms.CharField(max_length=10,required = True)
                
        class Meta(UserCreationForm.Meta):
                model = User
        
        def clean(self):
                super(StudentSignUpForm,self).clean()
                first_name = self.cleaned_data.get('first_name')
                last_name = self.cleaned_data.get('last_name')
                contact_no = self.cleaned_data.get('contact_no')

                if first_name is None:
                        self.errors['first_name'] = self.error_class(['Firstname can not be empty*'])
                elif len(first_name)<2:
                        self.errors['first_name'] = self.error_class(['Firstname should be of atleast 2 character length*'])
                elif first_name is None:
                        self.errors['last_name'] = self.error_class(['Lastname can not be empty*'])
                elif len(first_name)<2:
                        self.errors['last_name'] = self.error_class(['Lastname should be of atleast 2 character length*'])
                elif contact_no is None:
                        self.errros['contact_no'] = self.errro_class(['Contact can not be empty*'])
                elif len(contact_no)<10 or len(contact_no)>10:
                        self.errros['contact_no'] = self.errro_class(['Contact no. should be 10 digit long*'])
                
                return self.cleaned_data

        @transaction.atomic
        def save(self):
                user = super().save(commit = False)
                user.email = self.cleaned_data.get('email')
                user.is_student = True
                user.is_teacher = False
                user.save()
                student = Student.objects.create(user = user)
                student.first_name = self.cleaned_data.get('first_name')
                student.last_name = self.cleaned_data.get('last_name')
                # student.stu_roll_no = self.cleaned_data.get('roll_no')
                student.department = self.cleaned_data.get('department')
                student.contact_no = self.cleaned_data.get('contact_no')
                student.save()
                return student


class TeacherSignUpForm(UserCreationForm):
        first_name = forms.CharField(max_length=50,required = True)
        last_name = forms.CharField(max_length=50,required = True)
        email = forms.EmailField(max_length = 100)
        department = forms.ModelChoiceField(queryset=Department.objects.all(),required = True)
        
        class Meta(UserCreationForm.Meta):
                model = User

        def clean(self):
                super(TeacherSignUpForm, self).clean()
                first_name = self.cleaned_data.get('first_name')
                last_name = self.cleaned_data.get('last_name')
                
                if first_name is None:
                        self._errors['first_name'] = self.error_class(['Firstname can not be empty*'])
                elif first_name.isdigit():
                        self._errors['first_name'] = self.error_class(['Firstname can not be digit*'])
                elif len(first_name)<2:
                        self._errors['first_name'] = self.error_class(['Firstname should be of atleast 2 character length*'])
                elif last_name is None:
                        self._errors['last_name'] = self.error_class(['Lastname can not be empty*'])
                elif last_name.isdigit():
                        self._errors['last_name'] = self.error_class(['Lastname can not be digit*'])
                elif len(last_name)<2:
                        self._errors['last_name'] = self.error_class(['Lastname should be of atleast 2 character length*'])
                
                return self.cleaned_data

        @transaction.atomic
        def save(self):
                user = super().save(commit = False)
                user.email = self.cleaned_data.get('email')
                user.is_student = False
                user.is_teacher = True
                user.save()
                teacher = Teacher.objects.create(user = user)
                teacher.first_name = self.cleaned_data.get('first_name')
                teacher.last_name = self.cleaned_data.get('last_name')
                # teacher.teach_sub = self.cleaned_data.get('teach_sub')
                teacher.department = self.cleaned_data.get('department')
                teacher.save()
                return teacher