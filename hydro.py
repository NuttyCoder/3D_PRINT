import tkinter as tk
import sqlite3
import datetime

# GUI Setup
def setup_gui():
    root = tk.Tk()
    root.title("Hydroponics Farm Manager")
    tk.Label(root, text="Welcome to the Hydroponics Manager!").pack()
    # Add input fields, buttons, and displays for metrics
    root.mainloop()

# Sensor Reading (Placeholder)
def read_sensors():
    # Replace with actual sensor reading logic
    return {"temperature": 25.3, "humidity": 55.2, "ph_level": 6.5}

# Database Setup
def setup_database():
    conn = sqlite3.connect("hydroponics_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_time TEXT,
            temperature REAL,
            humidity REAL,
            ph_level REAL
        )
    """)
    conn.commit()
    conn.close()

# Save Data to Database
def log_data(data):
    conn = sqlite3.connect("hydroponics_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO metrics (date_time, temperature, humidity, ph_level)
        VALUES (?, ?, ?, ?)
    """, (datetime.datetime.now(), data['temperature'], data['humidity'], data['ph_level']))
    conn.commit()
    conn.close()

# Main Function
def main():
    setup_database()
    data = read_sensors()
    log_data(data)
    setup_gui()

if __name__ == "__main__":
    main()
