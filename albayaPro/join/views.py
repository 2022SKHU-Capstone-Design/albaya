from django.shortcuts import redirect, render
from .forms import *

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
# Create your views here.
def index(request) :
    signin_form = SigninForm
    return render(request, 'join/index.html', {'signin_form' : signin_form})

def signin(request):
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None :
            login(request, user)
            return redirect('myCalendar/myCalendar.html')
        else : 
            return HttpResponse("아이디 또는 비밀번호가 맞지 않습니다.")