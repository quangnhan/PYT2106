import requests

class Server():
    
    def __init__(self,url):
        self.url = url
    def get(self):
        response = requests.get(self.url)
        data = response.json()
        print(data)

    def get_user(self, max_age=None, min_age=None):
        response = requests.get(self.url)
        data = response.json()
        

    def get_user_by_id(self,id):
        response = requests.get(f'{self.url}/{id}')
        data = response.json()
        return data
    
    def create_user(self,data):
        response = requests.post(self.url,data = data)
        data = response.json()
        return data
    
    def edit_user(self,id, data):
        response = requests.get(f'{self.url}/{id}')
        data = response.json()
        data['age'] = data
        response = requests.put(f'{self.url}/{id}', data=data)
        # print(response)

    def delete_user(self,id):
        response = requests.delete(f'{self.url}/{id}')

if __name__ == '__main__':
    url = 'https://611ba73022020a00175a4615.mockapi.io/User'
    server = Server(url)
    # print(server.get())
    # id = '2'
    # print(server.get_user_by_id(id))

    # data = {
    #     'name': 'Quang',
    #     'age': 30,
    # }
    # print(server.create_user(data))

    # print(server.edit_user(7,20))
    print(server.delete_user(3))