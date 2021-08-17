import requests

url = "https://611ba6e422020a00175a460d.mockapi.io/users"
response = requests.get(url)
data = response.json()

print(data)