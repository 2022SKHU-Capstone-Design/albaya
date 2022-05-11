from unicodedata import name
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

#media
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name="index"),

    #signin
    path('signin', views.signin, name='signin'),
    path('', include('django.contrib.auth.urls')),
    #signup
    path('signup', views.signup, name='signup'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)