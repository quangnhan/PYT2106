import requests

url = 'https://611ba87422020a00175a461c.mockapi.io/users'
response = requests.get(url) 
data = response.json()

print(data)
