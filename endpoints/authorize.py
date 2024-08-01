from endpoints.endpoint_handler import EndpointHandler
import requests
import allure


class Authorize(EndpointHandler):
    @allure.step('Get a new token')
    def create_token(self, body, headers=None):
        """Authorization"""
        self.response = requests.post(
            f'{self.url}/authorize',
            json=body,
            headers=headers
        )
        self.json = self.response.json()
        self.token = self.json['token']
        return self.response

    @allure.step('Check token validity')
    def check_token(self, token, headers=None):
        self.response = requests.get(
            f'{self.url}/authorize/{token}',
            headers=headers
        )
        return self.response
