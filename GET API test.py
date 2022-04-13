import json
import requests

address = "https://gorest.co.in/public/v2/todos"
response = requests.get(address)
json_response = json.loads(response.text)

#print 20 data
print(json_response[0:20])