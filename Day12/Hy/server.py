import requests

class Server:
    __url = "https://611ba6e422020a00175a460d.mockapi.io/"

    def __init__(self):
        pass

    #Method get user

    def get_users(self):
        req = requests.get(f"{self.__url}/users")
        data = req.json()
        for i in data:
            if (data["max_age"] != "none" and data["min_age"] != "none"):
                return data


    #Viêt hàm get_by_id(id)

    def get_by_id_users(self,id):
        req =requests.get(f"{self.__url}/users/{id}")
        data = req.json()
        return data

    # Viêt hàm post(data)

    def post_users(self, data):
        req= requests.post(f"{self.__url}/users",data=data)
        data = req.json()
        return data

    # Viêt hàm put(id, data)
    def put(self,id, data):
        req= requests.post(f"{self.__url}/users/{id}",data=data)
        data = req.json()
        return data

    # Viêt hàm delete(id)
    def del_user_by_id(self,id):
        req =requests.delete(f"{self.__url}/users/{id}")
        data = req.json()
        return data
