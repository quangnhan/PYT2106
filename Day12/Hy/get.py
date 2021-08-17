import requests

API = 'https://611ba8eb22020a00175a462b.mockapi.io/user'
reponse = requests.get(API)
data = reponse.json()
print(data)