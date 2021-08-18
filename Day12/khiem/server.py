import requests

class Server:
    __url = 'https://611ba8a222020a00175a4620.mockapi.io'
    
    def __init__(self):
        pass
    
    def get_shopper(self):
        response = requests.get(f'{self.__url}/Shopper')
        data = response.json()
        return data
    
    def get_shopper_by_id(self, id):
        response = requests.get(f'{self.__url}/Shopper/{id}')
        data = response.json()
        return data

    def create_shopper(self,data):
        response = requests.post(f'{self.__url}/Shopper', data={})
        data = response.json()
        return data

    def edit_shopper(self, id, data):
        response = requests.put(f'{self.__url}/Shopper/{id}', data)
        data = response.json()
        return data

    def delete_shopper(self,id):
        response = requests.delete(f'{self.__url}/Shopper/{id}')
        data = response.json()
        return data

if __name__ == '__main__':
    id = 7

    data = {
    'name_shop': 'Stuart1',
    'address': 636,
    'City': 'Danan'
    }
    server = Server()
    # data = server.get_shopper()
    # get_id = server.get_shopper_by_id(id)
    # create_s = server.create_shopper(data)
    # edit_s = server.edit_shopper(id,data)
    delete_s = server.delete_shopper(id)

    print(delete_s)