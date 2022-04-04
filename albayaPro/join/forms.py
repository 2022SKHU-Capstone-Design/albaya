from dataclasses import field
from pyexpat import model
from django import forms
from .models import *
from django.contrib.auth.models import User

class SigninForm(forms.ModelForm):
    class Meta:
        model = User
        field = [ 'username', 'password']