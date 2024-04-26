import requests

APIkey = '164f21a71d86970c9d1a1d533009801f'
lat = 17.4435  # Decimal latitude
lon = 78.3499  # Decimal longitude

url = f'http://api.openweathermap.org/data/2.5/air_pollution?appid={APIkey}&lat={lat}&lon={lon}'

try:
    response = requests.get(url)
    data = response.json()

    carbonmono_Oxide = data['list'][0]['components']['co']
    nitroxide = data['list'][0]['components']['no']
    ammonium = data['list'][0]['components']['nh3']

    print('Carbon Monoxide (CO): ', carbonmono_Oxide)
    print('Nitrogen Oxide (NO): ', nitroxide)
    print('Ammonia (NH3): ', ammonium)

    # Function to categorize air quality based on pollutant concentration
    def categorize_pollutant(pollutant, value):
        if pollutant == 'CO':
            if value >= 301:
                return 'Hazardous (very dangerous)'
            elif value >= 201:
                return 'Very Unhealthy'
            elif value >= 151:
                return 'Unhealthy'
            elif value >= 101:
                return 'Unhealthy for Sensitive Groups'
            else:
                return 'Good'
        elif pollutant == 'NO':
            # Define ranges and categories for NO
            if value >= 201:
                return 'Very High'
            elif value >= 101:
                return 'High'
            else:
                return 'Low'
        elif pollutant == 'NH3':
            # Define ranges and categories for NH3
            if value >= 201:
                return 'High'
            elif value >= 101:
                return 'Moderate'
            else:
                return 'Low'

    # Print air quality categories for each pollutant
    print('Air Quality Category:')
    print('CO:', categorize_pollutant('CO', carbonmono_Oxide))
    print('NO:', categorize_pollutant('NO', nitroxide))
    print('NH3:', categorize_pollutant('NH3', ammonium))

except Exception as e:
    print('Error:', e)
