import os
import sqlite3

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(os.path.join(CURRENT_DIRECTORY, "database.db"))
        self.connection.text_factory = str
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS numbers (id INTEGER PRIMARY KEY, number BIGINT)")
    
    def select_max_number(self):
        self.cursor.execute("SELECT MAX(number) AS max_number FROM numbers")
        n = self.cursor.fetchone()
        return n["max_number"]
    
    def insert_number(self, number):
        self.cursor.execute(f"INSERT INTO numbers (number) VALUES ('{number}')")
        self.connection.commit()