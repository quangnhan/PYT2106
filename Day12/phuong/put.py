import requests


#get Data
id = 1
url = f"https://611ba8ad22020a00175a4622.mockapi.io/fruit_name/{id}"
response = requests.get(url)
data = response.json()


#Modify Data
data["colour"] = "mongoloid"
response = requests.put(url, data = data)
print(response)
