import requests

data = {
        'name': 'Ray',
        'age': '99'
        }
url = 'https://611ba87422020a00175a461c.mockapi.io/users'
response = requests.post(url, data=data) 
data = response.json()

print(data)
