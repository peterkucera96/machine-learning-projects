import psycopg2
import pandas as pd
import json
import matplotlib.pyplot as plt


def load_data():
    # Load config
    with open("../config/config.example.json") as f:
        cfg = json.load(f)

    # Connect to DB
    conn = psycopg2.connect(**cfg["db"])

    query = """
    SELECT city, temperature, humidity, pressure, wind_speed, timestamp
    FROM weather
    ORDER BY timestamp;
    """

    df = pd.read_sql(query, conn)
    conn.close()
    return df


def analyze(df):
    print("📊 BASIC DATA OVERVIEW")
    print(df.describe())

    print("\n🌡 Average temperature:")
    print(df["temperature"].mean())

    print("\n🔥 Maximum temperature:")
    print(df["temperature"].max())

    print("\n❄ Minimum temperature:")
    print(df["temperature"].min())


def plot_temperature(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df["timestamp"], df["temperature"])
    plt.title("Temperature over time")
    plt.xlabel("Timestamp")
    plt.ylabel("Temperature °C")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    df = load_data()
    analyze(df)
    plot_temperature(df)
