from django.contrib import admin
from django.urls import path

#media
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.store, name="store"),
    
    #공지
    path('notice/', views.notice, name="notice"),
    path('notice/write/', views.notice_write, name="notice_write"),
    path('notice/detail/<str:id>/', views.view_notice, name="notice_detail"),

    #건의
    path('suggest/', views.suggest, name="suggest"),
    path('suggest/write', views.suggest_write, name="suggest_write"),
    path('suggest/detail/<str:id>/', views.view_suggest, name="suggest_detail"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)