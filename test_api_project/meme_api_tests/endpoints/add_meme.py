import requests
import allure
from endpoints.endpoint_handler import EndpointHandler


class AddMeme(EndpointHandler):
    @allure.step('Create a new meme')
    def create_meme(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f'{self.url}/meme',
            json=body,
            headers=headers
        )
        return self.response
