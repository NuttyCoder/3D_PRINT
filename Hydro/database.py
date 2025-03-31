import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('hydroponics.db')
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS logs
                          (datetime TEXT, temperature REAL, humidity REAL, water_quality REAL)''')
        self.conn.commit()

    def log_data(self, temperature, humidity, water_quality):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO logs (datetime, temperature, humidity, water_quality) VALUES (?, ?, ?, ?)",
                       (datetime.now(), temperature, humidity, water_quality))
        self.conn.commit()

    def fetch_logs(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM logs ORDER BY datetime DESC")
        return cursor.fetchall()
