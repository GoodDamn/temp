import sqlite3 as sql
from typing import List

class Database():

    cursor: sql.Cursor
    connection: sql.Connection

    def __init__(self):
        self.connection = sql.connect("sigma.db")
        self.cursor = self.connection.cursor()
        
        pass

    def release(self):
        self.cursor.close()
        self.connection.close()

    def select(self, table: str) -> List[any]:
        self.query(
            f"select * from {table};"
        )
        return self.cursor.fetchall()

    def query(
        self,
        query: str) -> sql.Cursor:
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor
