class Schedule:
    __scheduleId = 0
    __date = ""
    __day = ""
    __time = ""
    __month = ""


    #def __init__(self, id, month, day, time, date):
        #self.__date = date
        #self.__day = day 
        #self.__time = time 
        #self.__month = month
        #self.__scheduleId = id

    def getId(self):
        return self.__scheduleId

    def getDate(self):
        return self.__date

    def getDay(self):
        return self.__day

    def getTime(self):
        return self.__time 

    def getMonth(self):
        return self.__month

    def setId(self, id):
        self.__scheduleId = id

    def setDate(self, date):
        self.__date = date 

    def setDay(self, day):
        self.__day = day

    def setTime(self, time):
        self.__time = time 

    def setMonth(self, month):
        self.__month = month

