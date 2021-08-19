import requests

data = {
    "name" : "duc",
    "age"  :  25,
}
url = "http://611d12f77d273a0017e2f612.mockapi.io/User"
response = requests.post(url, data =data)
data = response.json()
print(data)