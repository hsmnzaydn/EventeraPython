class Event:

    def __init__(self, eventName, eventDescription, startEventTime, endEventTime, eventSubCategorie,eventLocation):
        self.eventName = eventName
        self.eventDescription = eventDescription
        self.startEventTime = startEventTime
        self.endEventTime = endEventTime
        self.eventSubCategorie = eventSubCategorie
        self.eventLocation=eventLocation

    def returnEventName(self):
        return self.eventName

    def returnEventDescription(self):
        return self.eventDescription

    def returnEventStartTime(self):
        return self.startEventTime

    def returnEventEndTime(self):
        return self.endEventTime

    def returnCategoryName(self):
        return self.eventSubCategorie

    def returnLocation(self):
        return self.eventLocation

    def setCategoryName(self,name):
        self.eventSubCategorie=name