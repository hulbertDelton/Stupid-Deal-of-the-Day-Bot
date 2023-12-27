import requests
from bs4 import BeautifulSoup
#import datetime
from datetime import datetime, timedelta

musiciansfriendurl = "https://www.musiciansfriend.com/stupid"
channelid = 1170568462918221874

def GetDealInformation():
    page = requests.get(musiciansfriendurl)
    websoup = BeautifulSoup(page.content, "html.parser")
    primary = websoup.find(id = "primaryAvailability")
    return primary

def GetDealOfTheDayTitle():
    newdeal = GetDealInformation()
    dealname = newdeal.find(class_ = "displayNameColor").text.strip()
    strout = "__**MUSICIAN'S FRIEND STUPID DEAL OF THE DAY**__\n" + dealname
    return strout

def GetDealOfTheDayImage():
    newdeal = GetDealInformation()
    dealimage = newdeal.find(class_ = "sdBold").find('img').get('src')
    return dealimage

def GetDealOfTheDayText():
    newdeal = GetDealInformation()
    regularprice = newdeal.find(class_ = "regular-price").text.strip()
    savings = newdeal.find(class_ = "feature-save").find(class_ = "formatted-price").text.strip()
    dealprice = newdeal.find(class_ = "feature-price").find(class_ = "formatted-price").text.strip()
    description = newdeal.find(class_ = "feature-description").text.strip()
    enddate = newdeal.find(class_ = "feature-availability").find("strong").text.strip()
    strout = "\n" + description  + "\n\n"
    strout += "__Regular Price__: " + regularprice + "\n"
    strout += "__Savings__: " + savings  + "\n"
    strout += "__Deal Price__: " + dealprice + "\n"
    strout += enddate + "\n\n"
    strout += "**__GET IT HERE__**: " + musiciansfriendurl
    return strout

#print(GetDealOfTheDayTitle())
#print(GetDealOfTheDayImage())
#print(GetDealOfTheDayText())