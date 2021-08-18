import requests

id = 8
url = f'https://611ba87422020a00175a461c.mockapi.io/users/{id}'
response = requests.get(url) 
data = response.json()

data['name'] = 'NamelessIdiot'
data['age'] = '200'

resonse = requests.put(url, data=data)

print(data)
