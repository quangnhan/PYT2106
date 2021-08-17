import requests

# data with id=7
# {'name': 'foo', 'age': '6', 'id': '7'}
id = 7
url = f"https://611ba6e622020a00175a460f.mockapi.io/User/{id}"
r = requests.delete(url)
data = r.json()
print("[DEBUG] response: ", r)




