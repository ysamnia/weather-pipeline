import json
import sqlite3

# load raw JSON
with open("data/weather_raw.json", "r") as f:
    data = json.load(f)

# extract useful fields
timestamp = data["current"]["time"]
temperature = data["current"]["temperature_2m"]
humidity = data["current"]["relative_humidity_2m"]

# connect database
conn = sqlite3.connect("data/weather.db")

# create cursor
cursor = conn.cursor()

# insert row
cursor.execute("""
INSERT INTO weather (
    timestamp,
    temperature,
    humidity
)
VALUES (?, ?, ?)
""", (timestamp, temperature, humidity))

# save
conn.commit()

# close
conn.close()

print("weather loaded into database")