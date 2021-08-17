import requests

url = 'https://611ba6e622020a00175a460f.mockapi.io/User'
r = requests.get(url)
data = r.json()
print("[DEBUG] data: ", data)