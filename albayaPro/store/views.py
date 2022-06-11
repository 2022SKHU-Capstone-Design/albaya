from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *

# Create your views here.
def store(request) : 
    notice = Notice.objects
    suggestion = SuggestionBox.objects
    return render(request, 'store/store.html', {'notice':notice})

def notice(request) : 
    return render(request, 'store/noticeboard.html')

def suggest(request) : 
    return render(request, 'store/suggestboard.html')