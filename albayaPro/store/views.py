from django.shortcuts import render, redirect, get_object_or_404

from datetime import datetime
from django.utils.dateformat import DateFormat

from .models import *
from .forms import *

# Create your views here.

def store(request) : 
    #공지사항 / 건의사항 제목 가져오기
    notice = Notice.objects
    suggestion = SuggestionBox.objects

    #오늘 날짜가져오기
    year = DateFormat(datetime.now()).format('Y')
    month = DateFormat(datetime.now()).format('M')
    return render(request, 'store/store.html', {'notice':notice, 'suggest':suggest, 'year':year, 'month':month})

def notice(request) : 
    return render(request, 'store/noticeboard.html')

def suggest(request) : 
    return render(request, 'store/suggestboard.html')