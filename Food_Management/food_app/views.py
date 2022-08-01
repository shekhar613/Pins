from django.http import HttpResponse
from django.shortcuts import render
from requests import request
import json




# Create your views here.
def index(request):
    return render(request,"index.html")
