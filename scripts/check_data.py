import sqlite3

# connect
conn = sqlite3.connect("data/weather.db")

# cursor
cursor = conn.cursor()

# run SQL
cursor.execute("""
SELECT
timestamp,
temperature,
humidity
FROM weather
ORDER BY timestamp DESC
LIMIT 5
""")

# get results
rows = cursor.fetchall()

# show rows
for row in rows:
    print(row)

# close
conn.close()