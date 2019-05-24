import pandas
import requests, re
from bs4 import BeautifulSoup
l=[]
base_url = "https://www.makaan.com/pune-residential-property/buy-property-in-pune-city?page="
for page in range(2,150):
    print()
    r=requests.get(base_url+str(page)+".html")
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all=soup.find_all("div",{"class":"infoWrap"})
    for item in all:

        d = {}
        d["Price"]=item.find("span",{ "class":"val","itemprop":"offers"}).text
        d["Area"]=item.find("td",{"class":"size"}).text.replace(" ","")
        d["Status"]=item.find("td",{"class":"val"}).text

        try:
            d["Possession"]=item.find("li",{"class":"keypoint","title":"Possession by"}).text
        except:
            d["Possession"]="Not Available"
        try:
            d["Bathrooms"]=item.find("li",{"class":"keypoint","title":"Bathrooms"}).text
        except:
                d["Bathrooms"]="Not Available"
        try:
            d["Project Name"]=item.find("div",{"class":"title-line"}).find("span",{"class":"projName"}).text
        except:
                d["Project Name"]="Not Available"
        try:
                d["Address"]=item.find("span",{"itemprop":"addressLocality"}).text
        except:
            d["Address"]="Not Available"
        try:
             d["Rooms"]=item.find("div",{"class":"title-line"}).find("span",{"class":"val"}).text.replace(" ","")
        except:
            d["Rooms"]="Not Available"
        l.append(d)

df = pandas.DataFrame(l)
df.to_csv("Makaan.csv")
