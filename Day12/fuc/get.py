import requests
url = "https://611dc4867d273a0017e2f8e9.mockapi.io/human"
response = requests.get(url)
data = response.json()

print(data)

