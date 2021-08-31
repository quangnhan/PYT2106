import requests

class Server:
    __url = "https://611dc4867d273a0017e2f8e9.mockapi.io"
    def __init__(self):
        self.response = requests.get(f"{self.__url}/user")
        self.data = self.response.json()

    def get_Users(self, min_age= None, max_age= None):
        result = []
        for a in self.data: 
            if min_age <= int(a["age"]) <= max_age:
                result.append(a)
        return result
    def get_gmail(self):
        return requests.get(f"{self.__url}/email").json()

    def get_User_by_id(self, id):
        return requests.get(f"{self.__url}/user/{id}").json()

    def create_user(self, data):
        print(requests.post(f"{self.__url}/user",data))

    def edit_gmail_user(self, id, data):
        requests.put(f"{self.__url}/email/{id}", data=data)

    def edit_user(self, id, data):
        requests.put(f"{self.__url}/user/{id}", data=data)

    def delete_user(self, id):
        requests.delete(f"{self.__url}/user/{id}")

if __name__ == "__main__":
    server = Server()
    data = server.get_Users(10,20)
    print(data)
    print(server.get_User_by_id(1))
    user1 = {'name': "Phusc deeptry", 'age':int(17)}
    server.create_user(user1)
    server.edit_user(1,user1)
    server.delete_user(1)