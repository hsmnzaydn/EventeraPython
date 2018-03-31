from bs4 import BeautifulSoup
import requests
import Utility.Constant as Constant
import Utility.Utility as Utils
from models.Event import Event

eventList=[]


source = requests.get(Constant.TIME_OUT_BASE_URL+Constant.TIME_OUT_EVENTS_URL)
soup = BeautifulSoup(source.text, 'html.parser')
lastPage=soup.find('ul',attrs={'class':'pagination-list'}).findAll('a')
lastPageSize=lastPage[len(lastPage)-1].text

def getDetailOfEvent(url,eventName,eventSubCategorie):
    detailUrl=requests.get(url)
    detail = BeautifulSoup(detailUrl.text, 'html.parser')
    eventDescription=detail.find('div',attrs={'class':'readmore'}).text
    eventStartTime=detail.find('p',attrs={'class','has-text-grey'}).text
    eventLocation=detail.find('p',attrs={'class':'has-text-grey mt-05'}).text
    event=Event(eventName,eventDescription,eventStartTime,None,eventSubCategorie,eventLocation)
    eventList.append(event)


def getAllEvent(soup):
    listOfEvents = soup.findAll('div', attrs={'class': 'column is-4'})
    for event in listOfEvents:
        eventName=event.find('header',attrs={'class':'card-header'}).text
        eventSubCategorie=event.find('p',attrs={'class':'card-footer-item truncate'}).text
        eventDetailUrl=event.find('h3',attrs={'class':'card-header-title has-text-centered truncate'}).find('a',href=True)['href']
        getDetailOfEvent(eventDetailUrl,eventName,eventSubCategorie)





def getAllEvents():
    for page in range(int(lastPageSize)+1):
        if page is 0:
            continue
        source = requests.get(Constant.TIME_OUT_BASE_URL + Constant.TIME_OUT_EVENTS_URL+str(page))
        soup = BeautifulSoup(source.text, 'html.parser')
        getAllEvent(soup)


def getEventList():
    print('butcenegore.com parse ediliyor\n \n')
    getAllEvents()
    print('\n \nbutcenegore.com parse bitti')
    return eventList