from config.base_test import BaseTest
import requests



class TestSmgl(BaseTest):
    def test_create_session(self):
        session = self.api_smgl.create_session()
        print(session.session.id)


    def test_check_session(self):
        session = self.api_smgl.create_session()
        self.api_smgl.status_session(session.session.id)
