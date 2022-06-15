from bs4 import BeautifulSoup
import requests
import json,os

from Teaminterface.settings import BASE_DIR

def instaDownloader(url):
    return "getting data..."

def pinkIntrest(url):
    
    # urlo='https://pin.it/6nZW2Ja'
    # url=urlo
    site = requests.get(url)
    mainur=site.url
    id = mainur.split("/")[4]

    site = requests.get("https://www.pinterest.com/pin/"+id)
    mainur=site.url
    print(mainur)
    r=requests.get(mainur)
    soup=BeautifulSoup(r.content,'html.parser')
    script=soup.find('script',{"id":"__PWS_DATA__"}).text

    data=json.loads(script)

    
    Script_data = {"video_url":data["props"]["initialReduxState"]["pins"][id]["videos"]["video_list"]["V_720P"]["url"],
        "thumbnail":data["props"]["initialReduxState"]["pins"][id]["videos"]["video_list"]["V_720P"]["thumbnail"],
        "title":data["props"]["initialReduxState"]["pins"][id]["title"],
        "description":data["props"]["initialReduxState"]["pins"][id]["description"],
        "alloader":"Pintrest Downloader"
        }

    try:
        chunk_size = 256
        filename = id+'.mp4'
        Script_data["filename"] = filename
        base_dir = BASE_DIR
        r = requests.get(Script_data["video_url"],stream=True)
        print("path >> ",os.path.join(base_dir,"downloader/static/video"))
        with open(os.path.join(base_dir,"downloader/static/video",filename),"wb") as f:
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
    except Exception as E:
        print("Error >>> ",E)
    

    return Script_data



# print(pinkIntrest(""))
