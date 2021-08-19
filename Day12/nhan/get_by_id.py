import requests

id = 5
url = f"https://611ba6e422020a00175a460d.mockapi.io/users/{id}"
response = requests.get(url)
data = response.json()

print(data)