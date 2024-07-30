import requests
import allure
from enndpoints.endpoint_handler import EndpointHandler


class Authorize(EndpointHandler):

    @allure.step('Authorize and get token')
    def authorize(self, name):
        response = requests.post(
            f'{self.url}/authorize',
            json={'name': name}
        )
        response_json = response.json()
        self.token = response_json.get('token')
        return self.token

    def get_headers(self):
        headers = super().get_headers()
        if hasattr(self, 'token'):
            headers['Authorization'] = self.token
        return headers
