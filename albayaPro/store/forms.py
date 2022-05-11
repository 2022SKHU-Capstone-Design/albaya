from dataclasses import field
from pyexpat import model
from django import forms
from .models import *

class NoticeForm(forms.ModelForm) : 
    class Meta:
        model = Notice
        field = ['title', 'body']

class NoticeCommnetForm(forms.ModelForm) :
    class Meta:
        model = NoticeCommnet
        field = ['comment']

class SuggestionBoxForm(forms.ModelForm) :
    class Meta:
        model = SuggestionBox
        field = ['title', 'body']

class SuggestionCommnetForm(forms.ModelForm) :
    class Meta:
        model = SuggestionCommnet
        field = ['comment']