from re import L
from django.shortcuts import render

# Create your views here.
def storeCalendar(request) :
    return render(request, 'storeCalendar.html')
