import requests

url = 'https://611ba73022020a00175a4615.mockapi.io/User'

response = requests.get(url)
data = response.json()
print(data)
