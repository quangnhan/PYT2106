import requests

#Get Data
id = 1
url = f"https://611ba6e422020a00175a460d.mockapi.io/users/{id}"
response = requests.get(url)
data = response.json()

#Modifed data
data["age"] = 100
response = requests.put(url, data=data)
print(response)