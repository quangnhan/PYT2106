import requests

# data with id=7
# {'name': 'foo', 'age': '6', 'id': '7'}
id = 7
url = f"https://611ba6e622020a00175a460f.mockapi.io/User/{id}"
r = requests.get(url)
data = r.json()
print("[DEBUG] current data: ", data)

# update modified data to update name='bar' and age=100
data['name'] = 'bar'
data['age'] = 100
r = requests.put(
    url,
    data=data
)
print("[DEBUG] response: ", r)
print("[DEBUG] new data: ", requests.get(url).json())




