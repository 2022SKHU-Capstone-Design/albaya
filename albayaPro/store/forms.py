from django import forms
from .models import *

class NoticeForm(forms.ModelForm) : 
    class Meta:
        model = Notice
        fields = ['title', 'pub_date', 'body']

class NoticeCommnetForm(forms.ModelForm) :
    class Meta:
        model = NoticeCommnet
        fields = ['comment']

class SuggestionForm(forms.ModelForm) :
    class Meta:
        model = Suggestion
        fields = ['title', 'pub_date', 'writer', 'body']

class SuggestionCommnetForm(forms.ModelForm) :
    class Meta:
        model = SuggestionCommnet
        fields = ['comment']