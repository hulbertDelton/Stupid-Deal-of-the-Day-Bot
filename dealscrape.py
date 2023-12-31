import requests
from bs4 import BeautifulSoup

MUSICIANS_FRIEND_URL = "https://www.musiciansfriend.com/stupid"

def __GetDealInformation():
    page = requests.get(MUSICIANS_FRIEND_URL)
    if type(page) != requests.Response:
        print ("NO DATA RETURNED FROM SERVER")
        return
    websoup = BeautifulSoup(page.content, "html.parser")
    primary = websoup.find(id = "primaryAvailability")
    return primary

def GetDealOfTheDayTitle() -> str:
    newdeal = __GetDealInformation()
    try:
        dealname = newdeal.find(class_ = "displayNameColor").text.strip()
        return "**__" + dealname + "__**"
    except:
        print("NO SERVER DATA AVAILABLE FROM WEB REQUEST (title)")
        return ""

def GetDealOfTheDayImage():
    newdeal = __GetDealInformation()
    try:
        dealimage = newdeal.find(class_ = "sdBold").find('img').get('src')
        return dealimage
    except:
        print("NO SERVER DATA AVAILABLE FROM WEB REQUEST (image)")
        return ""

def GetDealOfTheDayText():
    newdeal = __GetDealInformation()
    regularprice: str = ""
    savings: str = ""
    dealprice: str = ""
    description: str = ""
    enddate: str = ""

    try:
        regularprice = newdeal.find(class_ = "regular-price").text.strip()
        savings = newdeal.find(class_ = "feature-save").find(class_ = "formatted-price").text.strip()
        dealprice = newdeal.find(class_ = "feature-price").find(class_ = "formatted-price").text.strip()
        description = newdeal.find(class_ = "feature-description").text.strip()
        enddate = newdeal.find(class_ = "feature-availability").find("strong").text.strip()
    except:
        print("NO SERVER DATA AVAILABLE FROM WEB REQUEST (text)")
        return
    strout = ["\n" + description  + "\n\n"]
    strout[0] += "__Regular Price__: " + regularprice + "\n"
    strout[0] += "__Savings__: " + savings  + "\n"
    strout[0] += "__Deal Price__: " + dealprice + " <<<\n\n"
    strout[0] += enddate + "\n\n"
    strout[0] += "**__GET IT HERE__**: " + MUSICIANS_FRIEND_URL
    
    if len(strout[0]) > 2000:
        strout[0] = description.split('\n')
        strout_start = ""
        strout_mid = ""
        i = 0
        strout_s = ""
        while i < len(strout[0]) and len(strout_start) < 2000:
            if strout[0][i] == '' and strout[0][i - 1] != '':
                strout_s += "\n"
            else:
                n = strout[0][i]
                strout_s += "- " + strout[0][i] + '\n'
            i += 1
        strout_start = strout_s[:len(strout_start) - len(strout[0][i - 1]) - 4]
        i -= 1
        while i < len(strout[0]):
            if strout[0][i] == '' and strout[0][i - 1] != '':
                strout_mid += "\n"
            else:
                m = strout[0][i]
                strout_mid += "- " + strout[0][i] + '\n'
            i += 1
        
        strout_end = f"__Regular Price__: {regularprice}\n__Savings__: {savings}\n__Deal Price__: {dealprice} <<<\n\n{enddate}\n\n**__GET IT HERE__**: {MUSICIANS_FRIEND_URL}"
        strout = [strout_start, strout_mid, strout_end]

    return strout

#print(GetDealOfTheDayTitle())
#print(GetDealOfTheDayImage())
#print(GetDealOfTheDayText())
#d = GetDealOfTheDayText()
#for s in d:
#    print(s)