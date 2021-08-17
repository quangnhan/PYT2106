import requests

data = ({
    'name': "phuong",
    'colour': "mongoloid",
    'id': 1
})
url = f"https://611ba8ad22020a00175a4622.mockapi.io/fruit_name/"
response = requests.get(url, data=data)
data = response.json()

print(data)
