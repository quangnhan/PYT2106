import requests
id = '2'
url = 'https://611ba73022020a00175a4615.mockapi.io/User/{}'.format(id)

response = requests.get(url)
data = response.json()

data['age'] = 30

response = requests.put(url, data=data)
print(response)

