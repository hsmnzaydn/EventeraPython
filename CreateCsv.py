
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
                tag=event.returnCategoryName()
                if tag=="Rock" or  tag=="Türk Sanat - Halk Müziği" or tag=="Pop" or tag=="Diğer Müzik" or tag=="Klasik" or tag=="Türk" or tag=="Caz" or tag=="Heavy Metal" or tag=="Rap" or tag== "Caz":
                    event.setCategoryName("Music")
                elif tag=="Latin - Tango" or tag == "Bale" or tag=="Sergi" or tag=="New Age" or tag == "Alternatif" or tag== "Tiyatro" or tag== "Aile Tiyatrosu" or tag=="Dans - Elektronik" or tag=="Sinema" or tag=="Tiyatro" or tag=="Gösteri" or tag=="Sirk" or tag=="Sergi" or tag=="Stand-Up" or tag=="Sinema":
                    event.setCategoryName("Arts")
                elif tag == "Atölye":
                    event.setCategoryName("Hobbies")
                elif tag== "Eğitim" or tag=="Aile" or tag=="MEB Onaylı Eğitim" or tag=="Konferans":
                    event.setCategoryName("Family & Education")
                writer.writerow({eventName : event.returnEventName(), eventDescription:event.returnEventDescription(),eventStartTime:event.returnEventStartTime(),eventEndTime:event.returnEventEndTime(),eventCategoryName:event.returnCategoryName(),eventLocation:event.returnLocation() })

