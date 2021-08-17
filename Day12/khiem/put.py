import requests


#Get Data
id = 1
url = f'https://611ba8a222020a00175a4620.mockapi.io/Shopper/{id}'
response = requests.get(url)
data = response.json()

#Modify Data
data['name_shop'] ="Stuart"
response = requests.put(url, data=data)
print(data)