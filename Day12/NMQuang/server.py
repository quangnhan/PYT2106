import requests


class Server:
    __url = f'https://611ba87422020a00175a461c.mockapi.io/users'

    def __init__(self):
        pass

    def get_users(self):
        response = requests.get(self.__url)
        data = response.json()
        return data

    def get_users_by_id(self, id):
        response = requests.get(f'{self.__url}/{id}')
        data = response.json()
        return data

    def create_user(self, data):
        response = requests.post(self.__url, data=data)
        data = response.json()
        return data

    def edit_user(self, id, data):
        response = requests.put(f'{self.__url}/{id}', data=data)
        data = response.json()
        return data
    
    def delete_user(self, id):
        response = requests.delete(f'{self.__url}/{id}')
        data = response.json()
        return data


def main():
    server = Server()
    print(server.get_users())
    print(server.get_users_by_id('8'))
    print(server.create_user(data={
        'name': 'NewUser',
        'age': '100'}))
    print(server.edit_user(id=1, data={
        'name': 'ModifiedUser',
        'age': '150'}))
    print(server.delete_user(3))


if __name__ == "__main__":
    main()
