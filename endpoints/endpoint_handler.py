import allure


class EndpointHandler:
    url = 'http://167.172.172.115:52355'
    headers = {'Content-Type': 'application/json', 'Authorization': None}
    token = None
    response = None
    json = None
    meme_id = None

    @allure.step('Check response code is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200, (
            f"Expected status code 200, got {self.response.status_code}"
        )

    @allure.step('Check response code is 400')
    def check_status_code_is_400(self):
        assert self.response.status_code == 400, (
            f"Expected status code 400, got {self.response.status_code}"
        )

    @allure.step('Check response code is 401')
    def check_status_code_is_401(self):
        assert self.response.status_code == 401, (
            f"Expected status code 401, got {self.response.status_code}"
        )

    @allure.step('Check response code is 403')
    def check_status_code_is_403(self):
        assert self.response.status_code == 403, (
            f"Expected status code 403, got {self.response.status_code}"
        )

    @allure.step('Check response code is 404')
    def check_status_code_is_404(self):
        assert self.response.status_code == 404, (
            f"Expected status code 404, got {self.response.status_code}"
        )

    @allure.step('Check response code is 500')
    def check_status_code_is_500(self):
        assert self.response.status_code == 500, (
            f"Expected status code 500, got {self.response.status_code}"
        )

    @allure.step('Check that id is equal to expected')
    def check_response_id_is_correct(self, meme_id):
        assert self.json['id'] == meme_id, (
            f"Expected id to be {meme_id}, got {self.json['id']}"
        )

    @allure.step('Check meme data is correct')
    def check_meme_data_matches(self, expected_data):
        response_data = self.response.json()
        assert (response_data['text'] ==
                expected_data['text']), "Text does not match"
        assert (response_data['url'] ==
                expected_data['url']), "URL does not match"
        assert (response_data['tags'] ==
                expected_data['tags']), "Tags do not match"
        assert (response_data['info'] ==
                expected_data['info']), "Info does not match"

    @allure.step('Check token is alive')
    def check_token_is_alive_and_contains_name(self):
        assert "Token is alive. Username is brishar" in self.response.text, (
            f"Expected response to contain 'Token is alive. "
            f"Username is brishar', got '{self.response.text}'"
        )
