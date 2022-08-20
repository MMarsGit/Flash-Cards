import sqlite3
import Debug.Debug as Debug
from sqlite3 import Error

class database:

    def __init__(self):
        db_file = r"./database.db"
        self.conn = sqlite3.connect(db_file)

        self.cardsTable = """CREATE TABLE IF NOT EXISTS cards(
            id integer PRIMARY KEY,
            status text NOT NULL,
            word text NOT NULL,
            translation text NOT NULL,
            timesCorrect text,
            dateNext text
        );
        """

    def create_table(self):
        try:
            c= self.conn.cursor()
            c.execute(self.cardsTable)
        except Error as e:
            print(e)

    def insert_time(self, status, word, translation):
        sql = '''INSERT INTO time(status, word, translation)
                 VALUES(?,?,?) '''
        cur = self.conn.cursor()
        card = (status, word, translation)
        cur.execute(sql, card)
        self.conn.commit()
        return cur.lastrowid