from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path

#media
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.calculator, name="calculator"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)