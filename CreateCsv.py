
# -*- coding: utf-8 -*- 
import csv
import Utility.Constant as Constant



def writeToCsv(eventList):
    myFile = open(Constant.CSV_NAME, 'w', newline='', encoding='utf-8')  
    with myFile:
        eventName='EventName'
        eventDescription='EventDescription'
        eventStartTime='EventStartTime'
        eventEndTime='EventEndTime'
        eventCategoryName='EventCategoryName'
        eventLocation='EventLocation'
        cloumns = [eventName, eventDescription,eventStartTime,eventEndTime,eventCategoryName,eventLocation]
        writer = csv.DictWriter(myFile, fieldnames=cloumns)    
        writer.writeheader()
        for event in eventList:
            writer.writerow({eventName : event.returnEventName(), eventDescription:event.returnEventDescription(),eventStartTime:event.returnEventStartTime(),eventEndTime:event.returnEventEndTime(),eventCategoryName:event.returnCategoryName(),eventLocation:event.returnLocation() })

