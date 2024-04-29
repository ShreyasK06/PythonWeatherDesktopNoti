import requests
from datetime import datetime
from win11toast import toast

url = "https://api.weather.gov/gridpoints/PHI/64,101/forecast"

response = requests.get(url)
result = "No Weather"

if response.status_code == 200:
    data = response.json()
    today_date = datetime.now().date()

    today_forecast = None
    for period in data['properties']['periods']:
        forecast_date = datetime.strptime(period['startTime'], '%Y-%m-%dT%H:%M:%S%z').date()
        if forecast_date == today_date:
            today_forecast = period
            break

    if today_forecast:
        result = "Weather forecast for today: ", "Weather: ", today_forecast['shortForecast'], "Temperature: ", today_forecast['temperature'], today_forecast['temperatureUnit']

    result = str(result)
    
    image = {
    'src': 'Untitled.ico',
    'placement': 'hero'
}
    
    toast("Live Weather Update",result,scenario="incomingCall",button="Dismiss")