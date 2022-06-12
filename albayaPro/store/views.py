from urllib import request
from django.shortcuts import render, redirect, get_object_or_404

from datetime import datetime
from django.utils import dateformat, timezone

from .models import *
from .forms import *

def store(request) : 
    #공지사항 / 건의사항 제목 가져오기
    notices = Notice.objects
    suggestions = Suggestion.objects

    #오늘 날짜가져오기
    year = dateformat(datetime.now()).format('Y')
    month = dateformat(datetime.now()).format('M')
    return render(request, 'store/store.html', {'notices':notices, 'suggestions':suggestions, 'year':year, 'month':month})

#Read
#공지사항 페이지
def notice(request) : 
    return render(request, 'store/noticeboard.html')

#공지글 내용보기
def view_notice(reqeust):
    notice = get_object_or_404(Notice, id = id)
    return render(request, 'store/view_notice.html')

#건의사항 페이지
def suggest(request) : 
    return render(request, 'store/suggestboard.html')

#건의글 내용보기
def view_suggest(request, id):
    suggest = get_object_or_404(Suggestion, id = id)
    return render(request, 'store/view_suggest.html', {'suggest':suggest})

#Create / Update / Delete
#공지글쓰기
def notice_write(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('notice')
    else:
        form = NoticeForm()
        return render(request, 'store/notice_wirte.html')

#공지글 수정하기
def update_notice(request, id):
    update_notice = Notice.objects.get(id = id)
    update_notice.title = request.POST['title']
    update_notice.pub_date = timezone.now()
    update_notice.body = request.POST['body']
    update_notice.save()
    return redirect('notice', update_notice.id)

#공지글 삭제하기
def delete_notice(request, id):
    delete_notice = Notice.objects.get(id = id)
    delete_notice.delete()
    return redirect('notice')

#건의글쓰기
def suggest_write(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('notice')
    else:
        form = SuggestionForm()
        return render(request, 'store/suggest_wirte.html')

#건의글 수정하기
def update_suggest(request, id):
    update_suggest = Suggestion.objects.get(id = id)
    update_suggest.title = request.POST['title']
    update_suggest.pub_date = timezone.now()
    update_suggest.body = request.POST['body']
    update_suggest.save()
    return redirect('notice', update_suggest.id)

#건의글 삭제하기
def delete_suggest(request, id):
    delete_suggest = Suggestion.objects.get(id = id)
    delete_suggest.delete()
    return redirect('suggest')