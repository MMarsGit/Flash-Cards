import sqlite3
import Debug.Debug as Debug
from sqlite3 import Error

class database:

    def __init__(self):
        db_file = r"./database.db"
        self.conn = sqlite3.connect(db_file)

        

    def create_table(self):
        Debug.log("Creating table")
        cardsTable = """CREATE TABLE IF NOT EXISTS cards(
            id integer PRIMARY KEY,
            status text NOT NULL,
            word text NOT NULL,
            translation text NOT NULL,
            repetitions text,
            nextAppearance text
        );
        """
        #timesCorrect text,
         #   dateNext text
        try:
            c= self.conn.cursor()
            c.execute(cardsTable)
        except Error as e:
            print(e)

    def delete_table(self):
        Debug.log("Deleting table")
        deleteCards = "DROP TABLE cards;"

        try:
            c=self.conn.cursor()
            c.execute(deleteCards)
        except Error as e:
            print(e)

    def insert_card(self, card):
        Debug.log("Inserting card to database")
        status = str(card.status)
        Debug.debug("Status: " + status)
        word = str(card.word)
        Debug.debug("Word: " + word)
        translation = str(card.translation)
        Debug.debug("translation: " + translation)

        sql = '''INSERT INTO cards(status, word, translation)
                 VALUES(?,?,?) '''
                 
        cur = self.conn.cursor()
        card = (status, word, translation)
        cur.execute(sql, card)
        self.conn.commit()
        return cur.lastrowid

    def get_first_record(self):
        firstRecord = "SELECT * FROM cards ORDER BY ROWID ASC LIMIT 1"

        cur = self.conn.cursor()
        cur.execute(firstRecord)
        self.conn.commit()

        return cur.fetchone()
    
    def get_last_row_id(self):
        lastRow = "SELECT * FROM cards ORDER BY id DESC LIMIT 1"

        cur = self.conn.cursor()
        cur.execute(lastRow)
        self.conn.commit()

        return cur.fetchone()

    def get_record(self, num):
        nextRecord = "SELECT * FROM cards WHERE id=?"
        
        cur=self.conn.cursor()
        cur.execute(nextRecord, str(num))
        self.conn.commit()
        return cur.fetchone()

    def updateRepetitions(self, repetitions, nextAppearance, cardname):
        statement = "UPDATE cards SET repetitions=?, nextAppearance=? WHERE word=?"

        cur=self.conn.cursor()
        cur.execute(statement, (repetitions, nextAppearance, cardname))
        self.conn.commit()
        return cur.fetchone()
