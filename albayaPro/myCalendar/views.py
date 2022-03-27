from django.shortcuts import render

# Create your views here.
def myCalendar(request) : 
    return render(request, 'myCalendar.html')