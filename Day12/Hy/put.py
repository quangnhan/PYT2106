import requests

#GET METHOD BY ID
id = 1
API = f"https://611ba8eb22020a00175a462b.mockapi.io/user/{id}"
reponse = requests.get(API)
data = reponse.json()

# PUT METHOD
data["name"] = "Bách Hy"

reponse = requests.put(API,data=data)
data = reponse.json()
print(data)