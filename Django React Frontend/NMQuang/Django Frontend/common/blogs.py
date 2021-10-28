import requests
from .server import Server


class Blog(Server):
    def get_all_blog(self):
        url = f'{self._endpoint}/blog'
        response = requests.get(url)
        return response.json()
