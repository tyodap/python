import requests
import json

address = "https://gorest.co.in/public/v2/users"
access_token = "33cae90ddb283fe77b8ed16bebb6d5c02b142263cacdbea61795352113ccf049"
header = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(access_token)
    }
obj = {
    'name': 'Test post',
    'gender': 'male',
    'email': 'test.post@15ce.com',
    'status': 'active' 
    }

response = requests.post(address, data=json.dumps(obj), headers=header)

print(response.text)
