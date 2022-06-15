from bs4 import BeautifulSoup
import requests
import json


def fun():
      
#   urlo=record
    urlo='https://pin.it/4aGyOxz'
    url=urlo
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

    downloadurl=data["props"]["initialReduxState"]["pins"][id]["videos"]["video_list"]["V_720P"]["url"]
    print({"video_url":downloadurl,"data":data["props"]["initialReduxState"]["pins"][id]})


fun()