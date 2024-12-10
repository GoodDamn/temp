
from database import Database

tableApplicantEvents = "applicantEvents"

class dbApplicantEvents():
    
    database = Database()

    def createForm(self,
        userId: int,
        eventId: int):
        
        self.database.query(
            f'''
            insert into {tableApplicantEvents} (
                userId,
                eventId
            ) values (
                {userId},
                {eventId}
            );
            '''
        )

    def createTable(self):
         self.database.query(
            f'''
                create table if not exists {tableApplicantEvents} (
                    id integer primary key autoincrement,
                    userId integer,
                    eventId integer
                );
            '''
        )