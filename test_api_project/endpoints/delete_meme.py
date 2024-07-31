import requests
import allure
from endpoints.endpoint_handler import EndpointHandler


class DeleteMeme(EndpointHandler):
    @allure.step('Delete a meme dy ID')
    def delete_meme(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f"{self.url}/meme/{meme_id}",
            headers=headers
        )
        return self.response

    @allure.step('Verify that meme is deleted')
    def check_deleted_meme_is_deleted(self, meme_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/meme/{meme_id}',
            headers=headers
        )
        assert self.response.status_code == 404, (
            f"Expected 404, got {self.response.status_code}"
        )
