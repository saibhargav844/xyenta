from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_weather():
    result_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        result_data = fetch_weather(city)
    return render_template('weather.html', result_data=result_data)

def fetch_weather(city):
    apiKey = "164f21a71d86970c9d1a1d533009801f"
    Basic_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{Basic_url}appid={apiKey}&q={city}"
    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        weather_data = response.json()
        if weather_data["cod"] != "404":
            main_info = weather_data["main"]
            weather_description = weather_data["weather"][0]["main"]
            wind = weather_data['wind']['speed']
            temperature = main_info["temp"]
            pressure = main_info['pressure']
            return {
                'temperature': temperature,
                'weather_description': weather_description,
                'pressure': pressure,
                'wind_speed': wind
            }
    except Exception as e:
        print('error message', e)
    return None

if __name__ == '__main__':
    app.run(debug=True)
