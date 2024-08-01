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

    @allure.step('Check that id is equal to expected')
    def check_response_id_is_correct(self, meme_id):
        assert self.json['id'] == meme_id, (
            f"Expected id to be {meme_id}, got {self.json['id']}"
        )

    @allure.step('Check response code is 400')
    def check_status_code_is_400(self):
        assert self.response.status_code == 400, (
            f"Expected status code 400, got {self.response.status_code}"
        )

    @allure.step('Check response code is 403')
    def check_status_code_is_403(self):
        assert self.response.status_code == 403, (
            f"Expected status code 403, got {self.response.status_code}"
        )
