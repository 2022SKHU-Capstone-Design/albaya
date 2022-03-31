from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', include('calculator.urls')),
    path('category/', include('category.urls')),
    path('', include('join.urls')),
    path('myCalendar/', include('myCalendar.urls')),
    path('store/', include('store.urls')),
]
