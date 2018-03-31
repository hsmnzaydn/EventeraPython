# -*- coding: utf-8 -*- 
from bs4 import BeautifulSoup
import requests
import Utility.Constant as Constant
import Utility.Utility as Utils
from models.Event import Event

eventList=[]




source = requests.get(Constant.IST_THEATRE_BASE_URL+Constant.IST_THEATRE_EVENT_LIST_URL)
soup = BeautifulSoup(source.text, 'html.parser')
listOfEvents=soup.findAll('div',attrs={'class':'white-box section-scope'})

def getDetailOfEvent(eventNumber):
    eventDetailPage=requests.get(Constant.IST_THEATRE_BASE_URL+Constant.IST_THEATRE_EVENT_DETAIL_URL+str(eventNumber))
    eventSoup= BeautifulSoup(eventDetailPage.text, 'html.parser')
    eventDetail=eventSoup.find('div',attrs={'class':'subject'}).text
    return Utils.getWithOutBaseUrlEventNumber('Konusu',eventDetail)

def getAllEvent():
    for event in listOfEvents:
        eventStartDateDay=event.find('time',attrs={'class':'variant-day'}).text
        eventInformations=event.findAll('div',attrs={'class':'table-cell description'})
        for eventSingle in eventInformations:
            eventStartDateTime=eventSingle.find('time').text
            eventTime=eventStartDateDay+" "+eventStartDateTime
            eventName=eventSingle.find('h6').text
            eventLocation=eventSingle.find('p').text
            eventSubCategorie="Arts "
            eventDetailPage=eventSingle.find('a')['href']
            eventDescription=getDetailOfEvent(Utils.getWithOutBaseUrlEventNumber('/Basket/Index/',eventDetailPage))
            event=Event(eventName,eventDescription,eventTime,None,eventSubCategorie,eventLocation)
            eventList.append(event)



def getEventList():
    print('Istanbul şehir devlet tiyatroları parse ediliyor\n \n')
    getAllEvent()
    print('\n \nIstanbul şehir devlet tiyatroları parse bitti')
    return eventList


