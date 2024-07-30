import requests
import allure
from endpoints.endpoint_handler import EndpointHandler


class UpdateMeme(EndpointHandler):
    @allure.step('Update already existing meme')
    def put_update_meme(self, meme_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            url=f'{self.url}/meme/{meme_id}',
            json=body,
            headers=headers,
        )
        self.json = self.response.json()
        self.meme_id = self.json['id']
        return self.response
