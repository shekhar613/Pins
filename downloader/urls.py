from django import views
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="Home"),
    path('download',views.download,name="download"),
    path('about',views.about_alloader,name="about_alloader"),
    path('tools',views.tools_alloader,name="tools_alloader"),
    path('works',views.works,name="works"),
    path('updates',views.updates,name="updates"),
]