import requests

data = {
    'name': 'ABC',
    'age':20,
}
url = 'https://611ba73022020a00175a4615.mockapi.io/User'

response = requests.post(url,data = data)
data = response.json()
print(data)
