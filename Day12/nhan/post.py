import requests

data = {
    "name" : "Nhan",
    "age" : 26,
}
url = "https://611ba6e422020a00175a460d.mockapi.io/users"
response = requests.post(url, data=data)
data = response.json()

print(data)