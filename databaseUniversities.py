
from database import Database

tableUniversities = "universities"

class dbUniversities():

    def createUniversity(self,
        name: str,
        desc: str):

        Database().query(
            f'''
                insert into {tableUniversities} (
                    name,
                    desc
                ) values (
                    \"{name}\",
                    \"{desc}\"
                );
            '''
        )

    def getUniversities(self):
        out = []
        cursor = Database().query(
            f'''
                select * from {tableUniversities};
            '''
        )

        result = cursor.fetchall()

        for row in result:
           out.append(
                {
                    "id": row[0],
                    "name": row[1],
                    "desc": row[2]
                }
            )
           
        return out

    def createTable(self):
        Database().query(
            f'''
                create table if not exists {tableUniversities} (
                    id integer primary key autoincrement,
                    name string,
                    desc string
                );
            '''
        )