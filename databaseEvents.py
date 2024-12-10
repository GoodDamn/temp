
from database import Database

tableEvents = "events"

class dbEvents():
    
    database = Database()

    def createEvent(
        self,
        name: str,
        desc: str,
        register: bool,
        university_id: int,
        date: int):

        self.database.query(
            f'''
                insert into {tableEvents} (
                    name,
                    desc,
                    register,
                    event_date,
                    university_id
                ) values (
                    '{name}',
                    '{desc}',
                    {register},
                    {date},
                    {university_id}
                );
            '''
        )

    def getEvents(self):
        out = []
        result = self.database.select(
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

    def getEventsByUniversity(
        self,
        univereId: int):

        out = []
        cursor = self.database.query(
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
        self.database.query(
            f"drop table if exists {tableEvents}"
        )
        self.database.query(
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
