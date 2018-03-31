
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
            name=event.returnCategoryName.split(' ')
            for tag in name:
                if tag=="Rock" or "Pop" or "Diğer" or "Klasik" or "Türk" or "Caz" or "Heavy" or "Rap":
                    event.setCategoryName("Music")
                elif tag == "Bale" or "Dans" or "Sinema" or "Tiyatro" or "Gösteri" or "Sirk" or "Sergi" or "Stand-Up" or "Sinema":
                    event.setCategoryName("Arts")
                elif tag == "Atölye":
                    event.setCategoryName("Hobbies")
                elif tag== "Eğitim" or "Aile" or "MEB":
                    event.setCategoryName("Family & Education")
                else:
                    event.setCategoryName("other")
            writer.writerow({eventName : event.returnEventName(), eventDescription:event.returnEventDescription(),eventStartTime:event.returnEventStartTime(),eventEndTime:event.returnEventEndTime(),eventCategoryName:event.returnCategoryName(),eventLocation:event.returnLocation() })

