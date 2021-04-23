import sqlite3 
from Backend.Schedule import Schedule

class ScheduleDBServices:
    __conn = ""

    #opens connection
    def open(self):
        self.__conn = sqlite3.connect('Schedule.db')
        print('schedule db open')


    #closes connection
    def close(self):
        self.__conn.close()
        print('schedule db closed')


    #inserts new schedule record into the database
    def insertSchedule(self, schedule, username):
        self.createSchedulesTable()
        self.createLinkTable()

        #Adds record into the schedules table
        scheduleSql = "INSERT INTO schedules (scheduleId, month, day, time, date) VALUES (?, ?, ?, ?, ?);"
        scheduleArguments = (schedule.getId(), schedule.getMonth(), schedule.getDay(), schedule.getTime(), schedule.getDate())
        self.__conn.execute(scheduleSql, scheduleArguments)
        self.__conn.commit()

        #gets the primary key of the newly inserted record
        id = schedule.getId()

        #Adds record immediately into the link table
        linkSql = "INSERT INTO EmployeeSchedules (scheduleId, username) VALUES (?, ?);"
        linkArguments = (id, username)
        self.__conn.execute(linkSql, linkArguments)
        self.__conn.commit()

        print('insert happened')


    #returns a list of schedule objects to be displayed in the ViewSchedule page
    def getSchedule(self, username):

        self.createSchedulesTable()
        self.createLinkTable()
        sql = '''   SELECT *
                    FROM Schedules, EmployeeSchedules 
                    WHERE EmployeeSchedules.scheduleId = Schedules.scheduleId
                    AND EmployeeSchedules.username = ? '''
        arguments = [username]
        cursor = self.__conn.execute(sql, arguments)

        schedule = Schedule()
        scheduleList = []

        for row in cursor:
            schedule.setId(row[0])
            schedule.setMonth(row[1])
            schedule.setDay(row[2])
            schedule.setTime(row[3])
            schedule.setDate(row[4])
            scheduleList.append(schedule) #adds the schedule into the list

        return scheduleList


    #creates schedule table 
    def createSchedulesTable(self):
        self.__conn.execute('''CREATE TABLE IF NOT EXISTS schedules
                            (scheduleId    PRIMARY KEY,
                             month          INT,
                             day            CHAR(100),
                             time           CHAR(100),
                             date           CHAR(100)); ''')
        #print('schedules table created')

    #Creates the link table for schedules
    def createLinkTable(self):
        self.__conn.execute(''' CREATE TABLE IF NOT EXISTS EmployeeSchedules
                                 ( scheduleId   INT         UNIQUE NOT NULL,
                                   username     CHAR(100)   UNIQUE NOT NULL,
                                   FOREIGN KEY (scheduleId) REFERENCES schedules(scheduleId));''')
        #print('link table created')

    def dropTables(self):
        sql1 = "DROP TABLE IF EXISTS schedules"
        sql2 = "DROP TABLE IF EXISTS EmployeeSchedules"
        self.__conn.execute(sql1)
        self.__conn.execute(sql2)