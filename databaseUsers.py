
from database import Database

tableUsers = "users"

class dbUsers():

    database = Database()

    def countUsers(self):
        cursor = self.database.query(
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

        cursor = self.database.query(
            f'''
            select id from {repo.tableUsers} where
                username = \"{model.username}\" and
                password = \"{model.password}\" and
                role = {model.role}
            '''
        )

        return cursor.fetchall()     

    def addUser(
        self,
        username: str,
        password: str,
        role: int):

        self.database.query(
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
        self.database.query(
            f'''create table if not exists {tableUsers} (
                id integer primary key autoincrement,
                username string,
                password string,
                date_register int,
                role tinyint
            );
            '''
        )