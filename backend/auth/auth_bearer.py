# auth/auth_bearer.py

def verify_token(token: str) -> bool:
    """
    Dummy function to verify a token.
    In a real application, you'd decode and verify the JWT.
    """
    # For demonstration, if the token starts with "token-", we assume it's valid.
    return token.startswith("token-")
