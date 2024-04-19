import requests
import json

api_key = "164f21a71d86970c9d1a1d533009801f"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

try:
    city_name = input("Enter city name: ")

    complete_url = base_url + f"appid={api_key}&q={city_name}"
    response = requests.get(complete_url)
    response.raise_for_status()  # Raise an exception for HTTP errors (e.g., 404)

    print("API Response:", response.text)  # Print API response for debugging

    weather_data = response.json()
    print(weather_data)

    if weather_data["cod"] != "404":
        main_info = weather_data["main"]
        current_temperature = main_info["temp"]
        current_pressure = main_info["pressure"]
        current_humidity = main_info["humidity"]

        weather_description = weather_data["weather"][0]["description"]
        

        print(f"Temperature (in Kelvin): {current_temperature:.2f}")
        print(f"Atmospheric pressure (in hPa): {current_pressure}")
        print(f"Humidity (in percentage): {current_humidity}")
        print(f"Description: {weather_description}")
    else:
        print("City Not Found")

except requests.RequestException as e:
    print("Error occurred during API request:", e)
except json.JSONDecodeError as e:
    print("Error decoding JSON response:", e)
except KeyError as e:
    print("KeyError occurred while accessing weather data:", e)
