from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserChangeForm
from django import forms
from account.models import User,Teacher
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
        model = Teacher
        fields = ['first_name','last_name','department','subject','image',]


    
