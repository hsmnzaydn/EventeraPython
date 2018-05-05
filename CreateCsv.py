
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
                tag=tag[3:-2]
                
                if tag=="Rock" or tag=="Müzikli Gösteri" or tag=="Türk Sanat - Halk Müziği" or tag=="Rap - Hiphop" or tag=="Pop" or tag=="Diğer Müzik" or tag=="Klasik" or tag=="Türk" or tag=="Caz" or tag=="Heavy Metal" or tag=="Rap" or tag== "Caz" or tag=="Dünya Müzik":
                    event.setCategoryName("Music")
                elif tag=="Science & Technology":
                    event.setCategoryName("Science & Technology")
                elif tag=="Sports & Fitness":
                     event.setCategoryName("Sports & Fitness")    
                elif tag=="Latin - Tango" or tag == "Bale - Dans" or tag=="Sergi" or tag=="New Age" or tag == "Alternatif" or tag== "Tiyatro" or tag== "Aile Tiyatrosu" or tag=='Dans - Elektronik' or tag=="Sinema" or tag=="Tiyatro" or tag=="Gösteri" or tag=="Sirk" or tag=="Sergi" or tag=="Stand-Up" or tag=="Sinema":
                    event.setCategoryName("Art")
                elif tag=="Fuar":
                    event.setCategoryName("Others")
                elif tag == "Atölye" or tag=="Hobbies & Special Interest":
                    event.setCategoryName("Hobbies")
                elif tag=="Business & Professional":
                     event.setCategoryName("Business & Professional")    
                elif tag=="Family & Education" or tag== "Eğitim" or tag=="Aile" or tag=="MEB Onaylı Eğitim" or tag=="Konferans" or tag == "Diğer Aile Eğlencesi":
                    event.setCategoryName("Family & Education")
                elif tag== "Basketbol" or tag=="Futbol" or tag=="Tenis" or tag == "Health & Wellness":
                    event.setCategoryName("Sport & Fitness")
                elif tag=="Community & Culture":
                     event.setCategoryName("Community")    
                elif tag == "Müze":
                    event.setCategoryName("Travel & Outdoor")
                elif tag=="Parti":
                    event.setCategoryName("Home & Lifestyle")
                else:
                    event.setCategoryName("Other")    
                writer.writerow({eventName : event.returnEventName(), eventDescription:event.returnEventDescription(),eventStartTime:event.returnEventStartTime(),eventEndTime:event.returnEventEndTime(),eventCategoryName:event.returnCategoryName(),eventLocation:event.returnLocation() })

