from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import *
# from django.contrib.auth.models import User

class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [ 'username', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'phone_number']