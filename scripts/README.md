# Weather Pipeline

Small data engineering practice project.

This project downloads weather data from Open-Meteo API, stores raw JSON files, loads useful fields into SQLite, and runs SQL analysis.

## Technologies

* Python
* SQLite
* SQL
* API (Open-Meteo)

## Project Structure

weather_pipeline/

* data/
* scripts/

## Pipeline

API → JSON → SQLite → SQL analysis

## How to Run

Create database:

python3 scripts/create_db.py

Run full pipeline:

python3 scripts/run_pipeline.py

Check results:

python3 scripts/check_data.py

## What I learned

* Calling APIs in Python
* Saving JSON files
* Loading data into databases
* SQL queries
* Basic automation