import requests
import allure
from enndpoints.endpoint_handler import EndpointHandler


class DeleteMeme(EndpointHandler):

    @allure.step('Delete meme by id')
    def delete_meme(self, meme_id):
        self.response = requests.delete(
            f'{self.url}/meme/{meme_id}',
            headers=self.get_headers()
        )
        self.response_json = self.response.json()
        return self.response
