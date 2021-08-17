import requests

class Server:
    __url = "https://611ba8ad22020a00175a4622.mockapi.io/"

    def __init__(self):
        pass

    def get_user(self):
        response = requests.get(f'{self.__url}/ruit_name/')
        data = response.json()
        return

    def get_by_id(self):
        response = requests.get(f"{self.__url}/fruit_name{id}")
        data = response.json()
        return

    def create_user(self):
        data = ({})
        url = f"{self.__url}"
        response = requests.post(url, data=data)
        data = response.json()
        return

    def edit_user(self, edit_data):
        self.edit_data = edit_data
        response = requests.put(f"{self.__url}", data = edit_data)
        print(response)
        return

    def delete_user(self):
        response = requests.delete(self.__url)
        data = response.json()
        return


if __name__ == "__main__":
    server = Server
    print(server.get_user())
    print(server.get_by_id('1'))
    print(server.create_user(data = {
        'name': "calcier",
        'age': '69',
        'id': '96'}))
    print(server.edit_user)