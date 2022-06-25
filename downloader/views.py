from django.http import HttpResponse
from django.shortcuts import render
from requests import request
from downloader import Scrapper




# Create your views here.
def index(request):
    data = {"alloader":"Downloader by alloader "}
    return render(request,"index.html",context=data)

def download(request):
    link = ""
    if request.method=="POST":
        url = request.POST.get('url','~')

        if("https://www.instagram.com" in url):
            link = Scrapper.instaDownloader(url)
        
        elif ("https://pin" in url):
            link = Scrapper.pinkIntrest(url)
            
        elif ("https://youtube" in url or "https://youtu.be" in url or "https://www.youtube" in url):
            link = Scrapper.youtube_down(url)
       
    return render(request,"downloader page.html",context=link)

def about_alloader(request):
    data = {}
    return render(request,"about_alloader.html",context=data)

def tools_alloader(request):
    data = {}
    return render(request,"tools.html",context=data)

def works():
    data = {}
    return render(request,"how_its_works.html",context=data)

def updates():
    data = {}
    return render(request,"updates.html",context=data)

