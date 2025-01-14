from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
API_KEY = ''
GOOGLE_MAPS_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

@app.route('/emergency-services', methods=['GET'])
def emergency_services():
    location = '20.8783,-156.6825'  # Latitude and Longitude for Lahaina, Maui
    radius = 5000  # Search radius in meters
    type_of_service = request.args.get('type')  # e.g., hospital, police

    if not type_of_service:
        return jsonify({'error': 'Missing required parameter: type'}), 400

    try:
        params = {
            'location': location,
            'radius': radius,
            'type': type_of_service,
            'key': API_KEY
        }
        response = requests.get(GOOGLE_MAPS_URL, params=params)
        
        print(f"Request URL: {response.url}")
        print(f"Response Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("Data received from Google Maps API:")
            print(data)  # Print the data received from the API
            
            services = []

            for place in data.get('results', []):
                service_info = {
                    'name': place.get('name'),
                    'address': place.get('vicinity'),
                    'rating': place.get('rating'),
                    'open_now': place.get('opening_hours', {}).get('open_now', 'N/A')
                }
                services.append(service_info)
            
            print("Formatted Emergency Services Data:")
            print(services)  # Print the formatted list of services

            return jsonify(services), 200
        else:
            print("Failed to fetch data from Google Maps API.")
            return jsonify({'error': 'Failed to fetch data from Google Maps API'}), response.status_code

    except Exception as e:
        print(f"Exception occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5007)
