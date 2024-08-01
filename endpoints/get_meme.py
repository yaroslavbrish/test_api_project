import requests
import allure
from endpoints.endpoint_handler import EndpointHandler


class GetMeme(EndpointHandler):
    @allure.step('Get a list of all memes')
    def get_all_memes(self, headers=None):
        self.response = requests.get(
            url=f'{self.url}/meme',
            headers=headers
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Get a meme by ID')
    def get_one_meme(self, meme_id, headers=None):
        self.response = requests.get(
            url=f'{self.url}/meme/{meme_id}',
            headers=headers
        )
        self.json = self.response.json()
        self.meme_id = self.json['id']
        return self.response
