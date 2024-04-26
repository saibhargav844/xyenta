import requests
import json

apiKey = "164f21a71d86970c9d1a1d533009801f"
Basic_url = "https://api.openweathermap.org/data/2.5/weather?"

result_data = []

try:
    city = input('enter the city:')
    complete_url = Basic_url + f"appid={apiKey}&q={city}"
    response = requests.get(complete_url)
    response.raise_for_status()

    weather_data = response.json()
    #print(weather_data)
    
    

    if weather_data["cod"]!="404":
        main_info = weather_data["main"]
        weather_description = weather_data["weather"][0]["main"]
        wind = weather_data['wind']['speed']
        temperature = main_info["temp"]
        pressure = main_info['pressure']
       

        print('current temeperatur:',temperature)
        print('weather_description:',weather_description)
        print('current pressure:',pressure)
        print('current wind speed:',wind)

    data = [temperature,weather_description,pressure,wind]
        # data.append(temperature,weather_description,pressure,wind)
    
except Exception as e:
    print('error message',e)

result_data.append(data)
print(result_data)