
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
                tag=event.returnCategoryName
                if tag=="Rock" or tag=="Pop" or tag=="Diğer" or tag=="Klasik" or tag=="Türk" or tag=="Caz" or tag=="Heavy" or tag=="Rap":
                    event.setCategoryName("Music")
                elif tag == "Bale" or tag=="Dans" or tag=="Sinema" or tag=="Tiyatro" or tag=="Gösteri" or tag=="Sirk" or tag=="Sergi" or tag=="Stand-Up" or tag=="Sinema":
                    event.setCategoryName("Arts")
                elif tag == "Atölye":
                    event.setCategoryName("Hobbies")
                elif tag== "Eğitim" or tag=="Aile" or tag=="MEB":
                    event.setCategoryName("Family & Education")
                else:
                    event.setCategoryName("other")
                writer.writerow({eventName : event.returnEventName(), eventDescription:event.returnEventDescription(),eventStartTime:event.returnEventStartTime(),eventEndTime:event.returnEventEndTime(),eventCategoryName:event.returnCategoryName(),eventLocation:event.returnLocation() })

