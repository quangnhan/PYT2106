import requests

id = '3'
url = 'https://611ba73022020a00175a4615.mockapi.io/User/{}'.format(id)

response = requests.get(url)
data = response.json()
print(data)
