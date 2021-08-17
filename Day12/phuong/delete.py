import requests

id = 1
url = f"https://611ba8ad22020a00175a4622.mockapi.io/fruit_name/{id}"
response = requests.delete(url)
data = response.json()

print(data)
