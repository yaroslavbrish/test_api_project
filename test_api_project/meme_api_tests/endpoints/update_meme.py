import requests
import allure
from enndpoints.endpoint_handler import EndpointHandler


class UpdateMeme(EndpointHandler):

    @allure.step('Update meme')
    def update_meme(self, meme_id, text, url, tags, info):
        payload = {
            'id': meme_id,
            'text': text,
            'url': url,
            'tags': tags,
            'info': info
        }
        self.response = requests.put(
            f'{self.url}/meme/{meme_id}',
            json=payload,
            headers=self.get_headers()
        )
        self.response_json = self.response.json()
        return self.response
