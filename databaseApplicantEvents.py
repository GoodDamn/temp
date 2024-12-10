
from database import Database

tableApplicantEvents = "applicantEvents"

class dbApplicantEvents():

    def createForm(self,
        userId: int,
        eventId: int):
        
        Database().query(
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
         Database().query(
            f'''
                create table if not exists {tableApplicantEvents} (
                    id integer primary key autoincrement,
                    userId integer,
                    eventId integer
                );
            '''
        )