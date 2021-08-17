import requests

data = ({
    'name': "phuong",
    'age': 25,
    'id': 1
})
url = f"https://611ba8ad22020a00175a4622.mockapi.io/fruit_name/"
response = requests.post(url, data=data)
data = response.json()

print(data)
