# from django.contrib import admin
from django.urls import path,include
from django.views import defaults
from downloader.views import *

urlpatterns = [
   path('',include('downloader.urls'))
]

defaults.page_not_found = error_404_view
