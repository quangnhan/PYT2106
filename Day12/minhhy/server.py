import requests

class Server:
    # private variable
    __url = 'https://611ba6e622020a00175a460f.mockapi.io'

    def __init__(self):
        pass

    def get_user(self):
        r = requests.get(f"{self.__url}/User")
        data = r.json()
        return data

    def get_user_by_id(self, id):
        r = requests.get(f"{self.__url}/User/{id}")
        if len(r.json()) > 0:
            return r.json()
        return 'Not Found'

    def create_user(self, data):
        r = requests.post(
            f"{self.__url}/User",
            data=data
        )
        return r

    def edit_user(self, id, age):
        data = self.get_user_by_id(id)
        print(data)
        data['age'] = age
        print(data)
        r = requests.put(
            f"{self.__url}/User/{id}",
            data=data
        )
        return r

    def delete_user(self, id):
        r = requests.delete(f"{self.__url}/User/{id}")
        return(r.json())

if __name__ == "__main__":
    server = Server()
    data = server.get_user()
    print("[DEBUG] data: ", data)

    # get_user_by_id
    id = 7
    print(server.get_user_by_id(id))

    # create_user
    data = {
        "name": "foo",
        "age": 200
    }
    print(server.create_user(data))

    # edit_user
    id = 7
    age = 300
    print(server.edit_user(id, age))

    # delete_user
    id = 7
    print(server.delete_user(id))