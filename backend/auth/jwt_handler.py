# auth/jwt_handler.py

import time

def create_token(data: dict) -> str:
    """
    Dummy function to create a token.
    In a real application, you'd use a library like python-jose to generate a JWT.
    """
    # For demonstration, we'll simply return a string with a timestamp.
    token = f"token-{data.get('username', 'user')}-{int(time.time())}"
    return token
