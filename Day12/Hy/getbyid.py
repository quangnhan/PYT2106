import requests

id = 1
API = f"https://611ba8eb22020a00175a462b.mockapi.io/user/{id}"
reponse = requests.get(API)
data = reponse.json()
print(data)