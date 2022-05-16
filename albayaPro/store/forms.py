from django import forms
from .models import *

class NoticeForm(forms.ModelForm) : 
    class Meta:
        model = Notice
        fields = ['title', 'body']

class NoticeCommnetForm(forms.ModelForm) :
    class Meta:
        model = NoticeCommnet
        fields = ['comment']

class SuggestionBoxForm(forms.ModelForm) :
    class Meta:
        model = SuggestionBox
        fields = ['title', 'body']

class SuggestionCommnetForm(forms.ModelForm) :
    class Meta:
        model = SuggestionCommnet
        fields = ['comment']