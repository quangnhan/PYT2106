import requests

data = {
    "name" : "Hy",
    "email" : "sdhsfsdgyast@gamil.com",
    "password" : "dshfsdhfjsd"
}
API = 'https://611ba8eb22020a00175a462b.mockapi.io/user'
reponse = requests.post(API,data=data)
data = reponse.json()
print(data)