from config.base_test import BaseTest



class TestSmgl(BaseTest):
    def test_create_session(self):
        self.api_smgl.create_session()


    def test_check_session(self):
        session = self.api_smgl.create_session()
        self.api_smgl.status_session(session)











    # def test_create_session(self):
    #     response = requests.post(
    #         url="https://proxy.demo.smgl.sh/api/v1/session/create",
    #         headers={
    #             "X-PARTNER-SIGN": "sign",
    #             "X-PARTNER-PROJECT": "alipay-test"
    #         },
    #         json={
    #             "amount_details": {
    #                 "amount":4700,
    #                 "currency": "HKD"
    #             },
    #             "metadata": "платеж через alipay"
    #         }
    #     )
    #     print(response.json())
    #     assert response.status_code == 200, response.json()