import requests
import json

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=52.3"
    "&longitude=6.75"
    "&current=temperature_2m,relative_humidity_2m"
)

response = requests.get(url)

data = response.json()

# save raw JSON to file
with open("data/weather_raw.json", "w") as f:
    json.dump(data, f, indent=2)

print("saved raw weather data")