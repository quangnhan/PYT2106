import requests

url = 'https://611ba8a222020a00175a4620.mockapi.io/Shopper'
response = requests.get(url)
data = response.json()


print(data)