import sqlite3

# create/connect database
conn = sqlite3.connect("data/weather.db")

# create cursor
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    temperature REAL,
    humidity INTEGER
)
""")

# save changes
conn.commit()

# close connection
conn.close()

print("database created")