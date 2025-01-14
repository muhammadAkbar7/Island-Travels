from flask import Flask, request, jsonify
import requests
from datetime import datetime
import calendar

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')
    days = request.args.get('days', default=1, type=int)
    if not location:
        return jsonify({'error': 'Location is required'}), 400
    if days < 1 or days > 16:
        return jsonify({'error': 'Days must be between 1 and 16'}), 400

    api_key = ''  # Replace with your actual API key
    current_weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial'
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt={days}&appid={api_key}&units=imperial'
    
    try:
        current_weather_response = requests.get(current_weather_url)
        forecast_response = requests.get(forecast_url)
        
        print(f"Current Weather Request URL: {current_weather_url}")
        print(f"Forecast Request URL: {forecast_url}")
        print(f"Current Weather Response Status Code: {current_weather_response.status_code}")
        print(f"Forecast Response Status Code: {forecast_response.status_code}")
        
        if current_weather_response.status_code == 200 and forecast_response.status_code == 200:
            current_weather_data = current_weather_response.json()
            forecast_data = forecast_response.json()
            
            print("Current Weather Data:")
            print(current_weather_data)  # Print current weather data
            print("Forecast Data:")
            print(forecast_data)  # Print forecast data
            
            current_weather_details = {
                'location': location,
                'temperature': current_weather_data['main']['temp'],
                'humidity': current_weather_data['main']['humidity'],
                'wind_speed': current_weather_data['wind']['speed'],
                'weather_description': current_weather_data['weather'][0]['description'],
                'date': datetime.now().strftime('%Y-%m-%d'),
                'time': datetime.now().strftime("%H:%M:%S")
            }

            forecast_details = {}
            for day in forecast_data['list']:
                date = datetime.fromtimestamp(day['dt'])
                day_name = calendar.day_name[date.weekday()]
                forecast_details[day_name] = {
                    'location': location,
                    'date': date.strftime('%Y-%m-%d'),
                    'temperature': day['temp']['day'],
                    'humidity': day['humidity'],
                    'wind_speed': day['speed'],
                    'weather_description': day['weather'][0]['description']
                }

            print("Formatted Current Weather Details:")
            print(current_weather_details)  # Print the formatted current weather details
            print("Formatted Forecast Details:")
            print(forecast_details)  # Print the formatted forecast details

            return jsonify({
                'current_weather': current_weather_details,
                'forecast': forecast_details
            })
        else:
            print("Error in fetching weather data.")
            print("Current Weather Response:")
            print(current_weather_response.json())  # Print current weather response error
            print("Forecast Response:")
            print(forecast_response.json())  # Print forecast response error

            return jsonify({
                'error': 'Failed to fetch weather data',
                'current_weather_status_code': current_weather_response.status_code,
                'current_weather_response': current_weather_response.json(),
                'forecast_status_code': forecast_response.status_code,
                'forecast_response': forecast_response.json()
            }), 500

    except Exception as e:
        print(f"Exception occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
