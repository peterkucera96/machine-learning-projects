CREATE TABLE IF NOT EXISTS weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    pressure INT,
    wind_speed FLOAT,
    weather_description VARCHAR(100),
    timestamp TIMESTAMP DEFAULT NOW()
);
