from django.http import HttpResponse
from django.shortcuts import render
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
            print(link)
        elif ("https://pin" in url):
            link = Scrapper.pinkIntrest(url)
            print(link)
            

            


            
    

    return render(request,"downloader page.html",context=link)


def about_alloader(request):
    return render(request,"about_alloader.html")