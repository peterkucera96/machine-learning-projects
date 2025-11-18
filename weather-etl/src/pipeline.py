# import json
# from extract import get_weather
# from transform import transform
# from load import load_to_db
#
# def main():
#     with open("../config/config.example.json") as f:
#         cfg = json.load(f)
#
#     for city in cfg["cities"]:
#         weather_raw = get_weather(cfg["api_key"], city)
#         weather_clean = transform(weather_raw)
#         load_to_db(weather_clean, cfg["db"])
#         print(f"Inserted weather for {city}")
#
#     print("ETL pipeline completed successfully for all cities.")
#
# if __name__ == "__main__":
#     main()
#

import json
import time

from extract import get_weather
from transform import transform
from load import load_to_db


def main():
    with open("../config/config.example.json") as f:
        cfg = json.load(f)

    cities = cfg.get("cities", [])
    if not cities:
        raise ValueError("No cities defined in config.json (key 'cities').")

    samples_per_city = cfg.get("samples_per_city", 1)

    total_records = len(cities) * samples_per_city
    print(f"Starting ETL pipeline: {len(cities)} cities × {samples_per_city} samples = {total_records} records\n")

    for i in range(samples_per_city):
        print(f"Batch {i + 1}/{samples_per_city}")

        for city in cities:
            try:
                weather_raw = get_weather(cfg["api_key"], city)
                weather_clean = transform(weather_raw)
                load_to_db(weather_clean, cfg["db"])
                print(f"Inserted weather for {city}")
            except Exception as e:
                print(f"Error for {city}: {e}")


            time.sleep(1)


        time.sleep(1)

    print("\nETL pipeline completed successfully.")


if __name__ == "__main__":
    main()

