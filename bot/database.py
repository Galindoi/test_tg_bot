# Simplified init script
import sqlite3

def init_db():
    conn = sqlite3.connect('petbot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        name TEXT,
        type TEXT,
        feeding_times TEXT
    )''')
    conn.commit()
    conn.close()
