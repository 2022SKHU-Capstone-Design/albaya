from django.shortcuts import render

# Create your views here.
def storeBoard(request) :
    return render(request, 'storeBoard.html')