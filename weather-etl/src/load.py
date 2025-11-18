import psycopg2

def load_to_db(data: dict, conn_params: dict):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()

    insert_query = """
    INSERT INTO weather (city, temperature, humidity, pressure, wind_speed, weather_description)
    VALUES (%s, %s, %s, %s, %s, %s);
    """

    cur.execute(insert_query, (
        data["city"],
        data["temperature"],
        data["humidity"],
        data["pressure"],
        data["wind_speed"],
        data["weather_description"]
    ))

    conn.commit()
    cur.close()
    conn.close()
