import requests
import allure
from enndpoints.endpoint_handler import EndpointHandler


class AddMeme(EndpointHandler):

    @allure.step('Add new meme')
    def add_meme(self, text, url, tags, info):
        payload = {
            'text': text,
            'url': url,
            'tags': tags,
            'info': info
        }
        self.response = requests.post(
            f'{self.url}/meme',
            json=payload,
            headers=self.get_headers()
        )
        self.response_json = self.response.json()
        return self.response
