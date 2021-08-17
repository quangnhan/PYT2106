import requests

id = 3
API = f"https://611ba8eb22020a00175a462b.mockapi.io/user/{id}"
reponse = requests.delete(API)
data = reponse.json()
