import random
from .redis_client import redis_client


def generate_confirmation_code(email):
    code = str(random.randint(100000, 999999))

    redis_client.setex(
        f"confirm_code:{email}",
        300,  
        code
    )

    return code


def verify_confirmation_code(email, code):
    saved_code = redis_client.get(f"confirm_code:{email}")

    if saved_code is None:
        return False

    if saved_code == code:
        redis_client.delete(f"confirm_code:{email}")
        return True

    return False