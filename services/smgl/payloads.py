from faker import Faker

fake = Faker()

class Payloads:
    @staticmethod
    def create_session(amount:str=4700, currency:str="HKD"):
        return {
            "amount_details": {
                "amount": amount,
                "currency": currency
            },
            "metadata": "платеж через alipay"
        }

    @staticmethod
    def status_session(session_id:str):
        return {
            "session_id": session_id
        }

