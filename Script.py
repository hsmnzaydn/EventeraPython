import CityTheatreOfIstanbul
import ButceneGoreParse
import  EventBriteParse
import CreateCsv

eventList=[]

eventList.extend(EventBriteParse.getEventList())
eventList.extend(CityTheatreOfIstanbul.getEventList())
eventList.extend(ButceneGoreParse.getEventList())




CreateCsv.writeToCsv(eventList)


