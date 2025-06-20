from faker import Faker

fake = Faker()

class Payloads:
    create_session = {
    "amount_details": {
        "amount":4700,
        "currency": "HKD"
    },
    "metadata": "платеж через alipay"
    }

    status_session = {
        "session_id": "ps_516607976"
    }

