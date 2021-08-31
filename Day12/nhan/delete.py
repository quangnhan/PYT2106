import requests

id = 2
url = f"https://611ba6e422020a00175a460d.mockapi.io/users/{id}"
response = requests.delete(url)
print(response)