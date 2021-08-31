import requests

id= 1
url = f"https://611dc4867d273a0017e2f8e9.mockapi.io/human/{id}"

response = requests.delete(url)