import sqlite3 
from Backend.Schedule import Schedule

class ScheduleDBServices:
    __conn = ""

    #opens connection
    def open(self):
        self.__conn = sqlite3.connect('Schedule.db')
        #print('schedule db open')


    #closes connection
    def close(self):
        self.__conn.close()
        #print('schedule db closed')

    def insert(self, schedule, username):
        self.createEmpSchedules()
        scheduleSql = "INSERT INTO EmpSchedules (scheduleId, month, day, time, date, username) VALUES (?, ?, ?, ?, ?, ?);"
        scheduleArguments = (schedule.getId(), schedule.getMonth(), schedule.getDay(), schedule.getTime(), schedule.getDate(), username)
        self.__conn.execute(scheduleSql, scheduleArguments)
        self.__conn.commit()


    def get(self, username):
        self.createEmpSchedules()
        sql = '''   SELECT *
                    FROM EmpSchedules 
                    WHERE username = ? '''

        arguments = [username]
        cursor = self.__conn.execute(sql, arguments)
        scheduleList = []

        for row in cursor:
            schedule = Schedule()
            schedule.setId(row[0])
            schedule.setMonth(row[1])
            schedule.setDay(row[2])
            schedule.setTime(row[3])
            schedule.setDate(row[4])
            scheduleList.append(schedule) #adds the schedule into the list

        return scheduleList

    def delete(self, username, date):
        sql = "DELETE FROM EmpSchedules WHERE username = ? AND date = ?"
        arguments = (username, date)
        self.__conn.execute(sql, arguments)
        self.__conn.commit()

    def createEmpSchedules(self):
        self.__conn.execute('''CREATE TABLE IF NOT EXISTS EmpSchedules
                            (scheduleId    PRIMARY KEY,
                             month          INT,
                             day            CHAR(100),
                             time           CHAR(100),
                             date           CHAR(100),
                             username       CHAR(100)); ''')

    def dropTables(self):
        sql1 = "DROP TABLE IF EXISTS schedules"
        sql2 = "DROP TABLE IF EXISTS EmployeeSchedules"
        sql3 = "DROP TABLE IF EXISTS EmpSchedules"
        self.__conn.execute(sql1)
        self.__conn.execute(sql2)
        self.__conn.execute(sql3)