import requests

class Server:
    __url = "https://611ba6e422020a00175a460d.mockapi.io"

    def __init__(self):
       pass

    def get_users(self):
        response = requests.get(f"{self.__url}/users")
        data = response.json()
        return data

if __name__ == "__main__":
    server = Server()
    data = server.get_users()
    print(data)