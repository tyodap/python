import requests
import json

address  = "https://gorest.co.in/public/v2/users"

response = requests.get(address)
json_response = json.loads(response.text)

for status in json_response:
    if status["status"] == "inactive":
        print(status)