from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = ''
HALEAKALA_PARK_CODE = 'hale'

@app.route('/park-alerts', methods=['GET'])
def get_park_alerts():
    park_code = request.args.get('park_code', HALEAKALA_PARK_CODE)
    nps_url = f"https://developer.nps.gov/api/v1/alerts?parkCode={park_code}&api_key={API_KEY}"
    
    try:
        response = requests.get(nps_url)
        print(f"Request URL: {nps_url}")
        print(f"Response Status Code: {response.status_code}")
        
        if response.status_code == 200:
            alerts_data = response.json()
            print("Data received from API:")
            print(alerts_data)  # Print the entire JSON response
            
            if 'data' in alerts_data and len(alerts_data['data']) > 0:
                alerts = [{
                    'title': alert['title'],
                    'description': alert['description'],
                    'category': alert['category'],
                    'url': alert['url']
                } for alert in alerts_data['data']]
                print("Formatted Alerts:")
                print(alerts)  # Print the formatted alerts data
                
                return jsonify({'park': 'Haleakalā National Park', 'alerts': alerts})
            else:
                print("No alerts found for the park.")
                return jsonify({'park': 'Haleakalā National Park', 'alerts': []}), 200
        else:
            print(f"Error: Failed to fetch park alerts. Status Code: {response.status_code}")
            return jsonify({'error': 'Failed to fetch park alerts', 'status_code': response.status_code}), 500
    except Exception as e:
        print(f"Exception occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
