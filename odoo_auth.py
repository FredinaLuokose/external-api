import requests
import json

# Define the Odoo API endpoint for authentication
url = 'http://localhost:8064/web/session/authenticate'
headers = {'Content-Type': 'application/json'}

# Define the authentication request payload
payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "db": "test1",
        "login": "admin",
        "password": "admin"
    },
    "id": 1
}


# Make the JSON-RPC request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("Response:", json.dumps(data, indent=4))
else:
    print("Error:", response.status_code, response.text)


