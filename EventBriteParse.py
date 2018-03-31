# -*- coding: utf-8 -*- 
import urllib.request, json
import Utility.Utility as Utils
from models.Event import Event
import Utility.Constant as Constant
import CreateCsv



eventList=[]



def getCategory(categoryId):
    eventSubCategoryId=Constant.EVENT_BRITE_BASE_URL+'/categories/'+str(categoryId)+'?token='+Constant.EVENT_BRITE_OAuth
    with urllib.request.urlopen(eventSubCategoryId) as url:
        data = json.loads(url.read().decode())
        print(data['name'])
        return data['name']
        

def getEventsInformations():
    eventsUrl=Constant.EVENT_BRITE_BASE_URL+'events/search/?location.address=Turkey&token='+Constant.EVENT_BRITE_OAuth
    with urllib.request.urlopen(eventsUrl) as url:
        data = json.loads(url.read().decode('utf-8'))
        return data['events']




def getAllEvent():
    for event in getEventsInformations():
        eventName=Utils.encode(event['name']['text'])
        eventDescription=Utils.encode(event['description']['text'])
        startEventTime=Utils.encode(event['start']['local'])
        endEventTime=Utils.encode(event['end']['local'])
        eventCategoryId=event['category_id']
        if eventCategoryId is not None:
            event=Event(eventName,eventDescription,startEventTime,endEventTime,getCategory(eventCategoryId),"Turkey")
        else:
            event=Event(eventName,eventDescription,startEventTime,endEventTime,"Genel","Turkey")
        eventList.append(event)


def getEventList():
    print('EventBrite parse ediliyor\n \n')
    getAllEvent()
    print('\n \nEventBrite parse bitti')
    return eventList
