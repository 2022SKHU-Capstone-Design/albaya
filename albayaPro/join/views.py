from django.shortcuts import redirect, render, get_object_or_404
from .forms import *
from .models import *

# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
# Create your views here.
def index(request) :
    signin_form = SigninForm
    return render(request, 'join/index.html', {'signin_form' : signin_form})

def signin(request) :
    if request.method == "POST" :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None :
            login(request, user)
            return redirect('myCalendar/')
        else : 
            return HttpResponse("아이디 또는 비밀번호가 맞지 않습니다.")

def signup(request) :
    if request.method == "POST" :
        form = UserForm(request.POST)
        if form.is_valid() :
            new_user = CustomUser.objects.create_user(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
                phone_number = form.cleaned_data['phone_number']
                )
            login(request, new_user)
            return redirect('myCalendar/')
    else :
        form = UserForm()
        return render(request, 'join/signup.html', {'form' : form})
