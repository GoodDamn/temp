
from database import Database
from models import UserInfo

tableUsers = "users"

class dbUsers():

    def countUsers(self):
        cursor = Database().query(
            f'''
                select count(*) from {tableUsers}
            '''
        )

        return cursor.fetchone()[0]

    def updateUserInfo(self,
        model: UserInfo,
        userId: int):
        Database().query(
            f'''
            update {tableUsers} set firstName = \"{model.firstName}\",
                surname = \"{model.surname}\",
                secondName = \"{model.secondName}\",
                isMale = {model.isMale}
                where id = {userId};
            '''
        )

    def getUserInfoById(self, 
        id: int):
        cursor = Database().query(
            f'''
            select * from {tableUsers} where
                id = {id}
            '''
        )

        r = cursor.fetchone()

        return {
            "id": r[0],
            "date": r[3],
            "firstName": r[5],
            "secondName": r[6],
            "surname": r[7],
            "isMale": r[8]
        }

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

    def dropTable(self):
        Database().query(
            f"drop table if exists {tableUsers}"
        )
    
    def createTable(self):
        Database().query(
            f'''create table if not exists {tableUsers} (
                id integer primary key autoincrement,
                username string,
                password string,
                date_register int,
                role tinyint,
                firstName string,
                secondName string,
                surname string,
                isMale bool
            );
            '''
        )