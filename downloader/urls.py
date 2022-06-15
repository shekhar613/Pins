from django import views
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="Home"),
    path('download',views.download,name="download"),
    path('about_alloader',views.about_alloader,name="about_alloader"),
]