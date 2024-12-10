
from database import Database

tableEvents = "events"

class dbEvents():

    def createEvent(
        self,
        name: str,
        desc: str,
        register: bool,
        university_id: int,
        date: int):

        Database().query(
            f'''
                insert into {tableEvents} (
                    name,
                    desc,
                    register,
                    event_date,
                    university_id
                ) values (
                    \"{name}\",
                    \"{desc}\",
                    {register},
                    {date},
                    {university_id}
                );
            '''
        )

    def deleteEventById(
        self,
        id: int):
        Database().query(
            f'''
                delete from {tableEvents} where
                    id = {id}
            '''
        )

    def getEvents(self):
        out = []
        result = Database().select(
            tableEvents
        )

        for row in result:
           out.append(
                {
                    "id": row[0],
                    "name": row[1],
                    "desc": row[2],
                    "register": row[3],  
                    "date": row[4],
                    "university_id": row[5]
                }
            )
           
        return out

    def getEventById(
        self,
        eventId: int):
        cursor = Database().query(
            f'''
                select * from {tableEvents} where
                    id = {eventId};
            '''
        )

        row = cursor.fetchone()

        return {
            "id": row[0],
            "name": row[1],
            "desc": row[2],
            "register": row[3],
            "date": row[4],
            "university_id": row[5]
        }

    def getEventsByUniversity(
        self,
        univereId: int):

        out = []
        cursor = Database().query(
            f'''
                select * from {tableEvents} where
                    university_id = {univereId};
            '''
        )

        result = cursor.fetchall()

        for row in result:
           out.append(
                {
                    "id": row[0],
                    "name": row[1],
                    "desc": row[2],
                    "register": row[3],  
                    "date": row[4],
                    "university_id": row[5]
                }
            )
           
        return out



    def createTable(self):
        Database().query(
            f'''create table if not exists {tableEvents} (
                id integer primary key autoincrement,
                name string,
                desc string,
                register bool,
                event_date int,
                university_id int
            );
            '''
        )
