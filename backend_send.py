import json
import requests 

url = "http://localhost:5000"  

# data = {'location': '[0.5,43.3]', 'people': '3', 'urgency':'green', 'description':'We did it!'}
data = {'sender': 'Alice', 'receiver': 'Bob', 'message':'We did it!'}

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

r = requests.post(url, data=json.dumps(data), headers=headers)
print(r)