import requests

id = 1
url = f"https://611ba6e622020a00175a460f.mockapi.io/User/{id}"
r = requests.get(url)
data = r.json()
print("[DEBUG] data: ", data)