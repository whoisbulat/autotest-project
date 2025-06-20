from services.smgl.api_smgl import SmglAPI


class BaseTest:

    def setup_method(self):
        self.api_smgl = SmglAPI()