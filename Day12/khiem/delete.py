import requests

id = 1
url = f'https://611ba8a222020a00175a4620.mockapi.io/Shopper/{id}'
response = requests.delete(url)
data = response.json()

print(data)