import requests

data = {
    'name_shop': 'Stuart',
    'address': 646,
    'City': 'Dana'
}
url = 'https://611ba8a222020a00175a4620.mockapi.io/Shopper'
response = requests.post(url, data=data)
data = response.json()


print(data)