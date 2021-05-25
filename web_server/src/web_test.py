import requests
import json

response = requests.get("http://127.0.0.1:5000/search")
json_data = json.loads(response.text)
print(json_data)

# response = requests.get("http://127.0.0.1:5000/delete/1393715618436706307")
# json_data = json.loads(response.text)
# print(json_data)


