from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', include('calculator.urls')),
    path('category/', include('category.urls')),
    path('join/', include('join.urls')),
    path('myCalendar/', include('myCalendar.urls')),
    path('storeBoard/', include('storeBoard.urls')),
    path('storeCalendar/', include('storeCalendar.urls')),
]
