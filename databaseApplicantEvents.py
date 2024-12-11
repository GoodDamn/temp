
from database import Database

tableApplicantEvents = "applicantEvents"

class dbApplicantEvents():

    def hasUserForm(
        self,
        eventId: int,
        userId: int) -> bool:

        cursor = Database().query(
            f'''
            select count(*) from {tableApplicantEvents} where
                eventId = {eventId} and
                userId = {userId} 
            '''
        )

        result = cursor.fetchone()

        return result[0] == 1

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