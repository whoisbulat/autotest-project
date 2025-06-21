import requests

from config.headers import Headers
from services.smgl.endpoints import Endpoints
from services.smgl.models.smgl_models import CreateSessionResponseModel
from services.smgl.payloads import Payloads
from utils.helper import Helper




class SmglAPI(Helper):
    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    def create_session(self):
        response = requests.post(
            url=self.endpoints.create_session,
            headers=self.headers.basic,
            json=self.payloads.create_session()
        )
        assert response.status_code == 200, response.json()
        model = CreateSessionResponseModel(**response.json())
        return model

    def status_session(self, session_id):
        response = requests.post(
            url=self.endpoints.status_session,
            headers=self.headers.basic,
            json=self.payloads.status_session(session_id)
        )
        return response.json()

