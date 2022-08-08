from django.http import HttpResponse
from django.shortcuts import render
from requests import request
from downloader import Scrapper
import json




# Create your views here.
def index(request):
    data = {"alloader":"Pinsdownloader"}
    return render(request,"index.html",context=data)

def download(request):
    link = ""
    if request.method=="POST":
        # url = request.POST.get('url','~')
        url = request.POST['link']

        if("https://www.instagram.com" in url):
            link = Scrapper.instaDownloader(url)
        
        elif ("https://pin" in url or "https://www.pinterest" in url):
            link = Scrapper.pinkIntrest(url)
            
        elif ("https://youtube" in url or "https://youtu.be" in url or "https://www.youtube" in url):
            link = Scrapper.youtube_down(url)
        else:
            link = {"error":"Invalid video url ! "}
    # return render(request,"downloader page.html",context=link)
  
    data = json.dumps(link)
    return HttpResponse(data)


def dashboard(request):
    pass


def error_404_view(request,exception):
    return render(request,"404.html",status=404)











def about_alloader(request):
    data = {}
    return render(request,"about_alloader.html",context=data)

def tools_alloader(request):
    name=""
    email=""
    data={}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
    
    
        data = {"name":name,"email":email}
        data = json.dumps(data)
        print(data)
        return HttpResponse(data)
    else:
        return render(request,"tools.html",context=data)
    

def works(request):
    data = {}
    return render(request,"how_its_works.html",context=data)

def updates(request):
    data = {}
    return render(request,"updates.html",context=data)
