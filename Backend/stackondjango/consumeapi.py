import requests
response = requests.get('http://127.0.0.1:8000/collections')

for data in response.json()['collections']:
    if data['sentiment'] == "Positive":
        print(data['open_price'])






