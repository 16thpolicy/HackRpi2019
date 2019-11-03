# import os
# cmd="python mongo_client.py"
# for i in range(40):
#     os.system(cmd)

import json
import requests 

url = "http://localhost:5000/allEvents"  

# url = "http://orllem.pythonanywhere.com/"

# data = {'location': '[0.5,43.3]', 'people': '3', 'urgency':'green', 'description':'We did it!'}
# data = {'sender': 'Alice', 'receiver': 'Bob', 'message':'We did it!'}

# headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# r = requests.get(url, data=json.dumps(data), headers=headers)

response = requests.get(
    url,
    params={"radius": 8.0,
        "x": 10.2,
        "y": 11.3 },
)
# print(r)