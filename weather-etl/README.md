# Weather ETL Pipeline (OpenWeather → PostgreSQL)

This project is a simple **ETL (Extract–Transform–Load) pipeline** built in Python.  
It periodically fetches weather data from the **OpenWeather API**, transforms it into a clean structure, and stores it in a **PostgreSQL** database for further analytics and reporting.

The goal is to demonstrate a basic **data engineering workflow**:
- calling an external API  
- transforming JSON data  
- loading it into a relational database  
- enabling historical analysis, visualisation, and dashboards  

---

## Features

- Extracts weather data for a selected city (or multiple cities)
- Cleans and transforms the data into a structured format
- Loads data into a PostgreSQL table
- Supports repeated runs → builds a historical dataset
- Includes Python analysis script (`analysis.py`)
- Works with Jupyter Notebook for visualization
- Config-based architecture (no secrets in code)
- Clean ETL separation: **extract → transform → load**

---

## Installation

1. Clone the repo
```bash
git clone 
cd weather-etl
```

2. Create and activate virtual environment
```bash
python3 -m venv venv/weather-etl
source venv/weather-etl/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create PostgreSQL database and table
```bash
CREATE DATABASE weatherdb;
```
Then run the content of sql/create_tables.sql inside that database.

---

## Architecture

**E – Extract:**  
`extract.py` calls the OpenWeather API and retrieves raw JSON with current weather data for a selected city.

**T – Transform:**  
`transform.py` parses the JSON and keeps only relevant fields (temperature, humidity, pressure, etc.).

**L – Load:**  
`load.py` inserts the transformed data into a PostgreSQL table `weather`.

**Pipeline runner:**  
`pipeline.py` orchestrates the whole flow (E → T → L).

---

## Tech Stack

- **Python** (3.x)  
- **PostgreSQL**  
- **psycopg2-binary** – PostgreSQL driver for Python  
- **requests** – for calling the OpenWeather API  

---

## Data Analysis
To analyze the collected weather data:

1. Run the Python analysis script
```bash 
python3 src/analysis.py
```
This script:
* loads data from PostgreSQL
* prints descriptive statistics
* displays min/max/average temperatures
* generates a temperature-over-time graph

---

## Project Structure

```bash
weather-etl/
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── pipeline.py
│   └── analysis.py
├── config/
│   ├── config.example.json
├── sql/
│   └── create_tables.sql
├── analysis.ipynb
├── requirements.txt
└── README.md

```



