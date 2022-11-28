from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User,AbstractUser

class Department(models.Model):
    department_id = models.IntegerField(primary_key = True)
    department_name = models.CharField(max_length = 50,blank = True)

    def __str__(self): 
        return str(self.department_name)

class Subject(models.Model):
    subject_id = models.CharField(max_length = 50,primary_key = True)
    subject_name = models.CharField(max_length = 50,blank = True)
    semester = models.CharField(max_length=10,blank = True)    
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE,blank = True)

    def __str__(self): 
        return str(self.subject_name)

class User(AbstractUser):
    last_login = models.DateField(default=timezone.now)
    is_teacher = models.BooleanField(default = False)
    is_student = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = True)
    is_active = models.BooleanField(default = True)
    email = models.EmailField(unique =True)
    
    def __str__(self): 
        return str(self.pk)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name = models.CharField(max_length=50,blank = True)
    last_name = models.CharField(max_length=50,blank = True)
    roll_no = models.CharField(max_length=10,blank = True)
    semester = models.CharField(max_length=10,blank = True)
    contact_no = models.IntegerField(blank = True,null=True)
    image = models.ImageField(upload_to="images/",null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)

    def __str__(self): 
        return str(self.first_name) 

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    first_name = models.CharField(max_length=50,blank = True)
    last_name = models.CharField(max_length=50,blank = True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to="images/",null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)
     
        
    def __str__(self): 
        return str(self.first_name)

    
