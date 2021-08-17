import requests

id = '1'
url = 'https://611ba73022020a00175a4615.mockapi.io/User/{}'.format(id)

response = requests.delete(url)
print(response)
