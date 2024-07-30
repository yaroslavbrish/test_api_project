import allure


class EndpointHandler:
    url = 'http://167.172.172.115:52355'
    response = None
    response_json = None
    headers = {'Content-type': 'application/json'}

    def get_headers(self):
        return self.headers

    @allure.step('Verify status code is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, f"Status code is not 200, got {self.response.status_code}"

    @allure.step('Verify response contains expected text')
    def check_response_contains(self, text):
        assert text in self.response_json.get('text', ''), f"Response does not contain expected text: {text}"

    def parse_response(self):
        try:
            self.response_json = self.response.json()
        except ValueError:
            self.response_json = None
            assert False, f"Failed to decode JSON response: {self.response.text}"
