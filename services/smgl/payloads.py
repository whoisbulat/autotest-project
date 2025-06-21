from faker import Faker

fake = Faker()

class Payloads:
    @staticmethod
    def create_session(amount=4700, currency="HKD"):
        return {
            "amount_details": {
                "amount": amount,
                "currency": currency
            },
            "metadata": "платеж через alipay"
        }

    @staticmethod
    def status_session(session_id):
        return {
            "session_id": session_id
        }

