import requests

url = f"https://611ba8ad22020a00175a4622.mockapi.io/fruit_name"
response = requests.get(url)
data = response.json()

print(data)
