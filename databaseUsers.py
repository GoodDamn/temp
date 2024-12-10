
from database import Database

tableUsers = "users"

class dbUsers():

    def countUsers(self):
        cursor = Database().query(
            f'''
                select count(*) from {tableUsers}
            '''
        )

        return cursor.fetchone()[0]

    def findUsers(
        self,
        username: str,
        password: str,
        role: int):

        cursor = Database().query(
            f'''
            select id from {tableUsers} where
                username = \"{username}\" and
                password = \"{password}\" and
                role = {role}
            '''
        )

        return cursor.fetchall()     

    def addUser(
        self,
        username: str,
        password: str,
        role: int):

        Database().query(
            f'''
            insert into {tableUsers} (
                username,
                password,
                date_register,
                role
            ) values (
                \"{username}\",
                \"{password}\",
                DateTime('now'),
                {role}
            );
            '''
        )

        pass

    def createTable(self):
        Database().query(
            f'''create table if not exists {tableUsers} (
                id integer primary key autoincrement,
                username string,
                password string,
                date_register int,
                role tinyint
            );
            '''
        )