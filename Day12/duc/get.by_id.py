import requests
id = 5
url = f"http://611d12f77d273a0017e2f612.mockapi.io/User{id}"
response = requests.get(url)
data = response.json()
print(data)