
from database import Database

tableUniversities = "universities"

class dbUniversities():

    database = Database()

    def createUniversity(self,
        name: str,
        desc: str):

        self.database.query(
            f'''
                insert into {tableUniversities} (
                    name,
                    desc
                ) values (
                    {name},
                    {desc}
                );
            '''
        )

    def createTable(self):
        self.database.query(
            f'''
                create table if not exists {tableUniversities} (
                    id integer primary key autoincrement,
                    name string,
                    desc string
                );
            '''
        )