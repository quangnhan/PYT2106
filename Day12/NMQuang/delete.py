import requests

id = 12
url = f'https://611ba87422020a00175a461c.mockapi.io/users/{id}'
response = requests.get(url) 
data = response.json()

response = requests.delete(url)

print(data)
