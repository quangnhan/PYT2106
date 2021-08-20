import requests

url = "https://611dc4867d273a0017e2f8e9.mockapi.io/human"

data = {"name": "phúc deeptry", 'age': 30}

response = requests.post(url, data = data)

print(response)