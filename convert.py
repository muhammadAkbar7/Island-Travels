import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key from ExchangeRate-API
API_KEY = ''
API_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'

@app.route('/convert', methods=['GET'])
def convert_currency():
    from_currency = request.args.get('from')
    to_currency = request.args.get('to')
    
    # Validate that required parameters are provided
    if not from_currency or not to_currency:
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        amount = float(request.args.get('amount'))
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid amount'}), 400

    # Fetch exchange rates from the API
    response = requests.get(API_URL + from_currency)
    
    print(f"Request URL: {API_URL + from_currency}")
    print(f"Response Status Code: {response.status_code}")
    
    if response.status_code != 200:
        print("Error fetching exchange rates.")
        return jsonify({'error': 'Error fetching exchange rates'}), 500

    data = response.json()
    print("Data received from API:")
    print(data)  # Print the data received from the API

    if 'conversion_rates' not in data or to_currency not in data['conversion_rates']:
        print("Conversion rate not found.")
        return jsonify({'error': 'Conversion rate not found'}), 400

    conversion_rate = data['conversion_rates'][to_currency]
    converted_amount = amount * conversion_rate

    print("Conversion Details:")
    print({
        'from': from_currency,
        'to': to_currency,
        'original_amount': amount,
        'converted_amount': converted_amount,
        'rate': conversion_rate
    })  # Print the conversion details

    return jsonify({
        'from': from_currency,
        'to': to_currency,
        'original_amount': amount,
        'converted_amount': converted_amount,
        'rate': conversion_rate
    })

if __name__ == '__main__':
    app.run(debug=True, port=5005)
