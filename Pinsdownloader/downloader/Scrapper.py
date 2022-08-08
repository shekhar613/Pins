from bs4 import BeautifulSoup, Script
import requests
import json,os
from pytube import YouTube

from Teaminterface.settings import BASE_DIR

def instaDownloader(url):
    Script_data={}
    Script_data['error']=f"Downloader is now unvailable !"
    return Script_data

def pinkIntrest(url):
    Script_data={}
    try:

        # urlo='https://pin.it/6nZW2Ja'
        # url=urlo
        site = requests.get(url)
        mainur=site.url
        id = mainur.split("/")[4]

        site = requests.get("https://www.pinterest.com/pin/"+id)
        mainur=site.url
        r=requests.get(mainur)
        soup=BeautifulSoup(r.content,'html.parser')
        script=soup.find('script',{"id":"__PWS_DATA__"}).text

        data=json.loads(script)

        Script_data = {"Pinstory":0,"video_url":data["props"]["initialReduxState"]["pins"][id]["videos"]["video_list"]["V_720P"]["url"],
            "thumbnail":data["props"]["initialReduxState"]["pins"][id]["videos"]["video_list"]["V_720P"]["thumbnail"],
            "title":data["props"]["initialReduxState"]["pins"][id]["title"],
            "alloader":"Pintrest Downloader",
            "error":""
            }

        chunk_size = 256
        filename = id+'.mp4'
        Script_data["filename"] = filename
        base_dir = BASE_DIR
        r = requests.get(Script_data["video_url"],stream=True)
        with open(os.path.join(base_dir,"downloader/static/video",filename),"wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    
    except Exception as PinError:
        try:
            
            data=json.loads(script)
            title = data['props']['initialReduxState']["pins"]["511088257719512841"]["grid_title"]
            
            urls = []
            thumbnails=[]
            for i in data['props']['initialReduxState']["pins"]["511088257719512841"]["story_pin_data"]["pages"]:
                urls.append(i["blocks"][0]["video"]["video_list"]["V_EXP5"]["url"])
                thumbnails.append(i["blocks"][0]["video"]["video_list"]["V_EXP5"]["thumbnail"])

            Script_data = {"Pinstory":1, "video_url":urls, "thumbnail":thumbnails, "title":title,
                      "error":""}



        except Exception as StoryError:
            Script_data['error']=f"Invalid video url !{PinError} or {StoryError}"

    return Script_data


def youtube_down(url):
    Script_data={}
    try:
        my_video = YouTube(url)

        Script_data = {"Pinstory":0,"filename":"ddn.mp4","thumbnail":my_video.thumbnail_url,
            "title":my_video.title,
            "description":"To long...",
            "alloader":"YouTube Downloader",
            "error":""
            }

        base_dir = BASE_DIR
        my_video = my_video.streams.get_highest_resolution()
        my_video.download(output_path=os.path.join(base_dir,"downloader/static/video"),filename="ddn.mp4")
    except Exception as YtError:

        Script_data["error"] = f"Invalid video url !{YtError} "

    return Script_data
# print(pinkIntrest(""))
