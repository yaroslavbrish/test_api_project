import requests
import allure
from enndpoints.endpoint_handler import EndpointHandler


class GetMeme(EndpointHandler):

    @allure.step('Get list of all memes')
    def get_all_memes(self):
        self.response = requests.get(
            f'{self.url}/meme',
            headers=self.get_headers()
        )
        self.response_json = self.response.json()
        return self.response

    @allure.step('Get single meme by id')
    def get_meme(self, meme_id):
        self.response = requests.get(
            f'{self.url}/meme/{meme_id}',
            headers=self.get_headers()
        )
        self.response_json = self.response.json()
        return self.response
