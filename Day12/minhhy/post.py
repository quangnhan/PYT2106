import requests

data = {
    "name": "foo",
    "age": 6
}
url = 'https://611ba6e622020a00175a460f.mockapi.io/User'
r = requests.post(
    url,
    data=data
)
data = r.json()
print("[DEBUG] data: ", data)