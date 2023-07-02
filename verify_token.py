import secrets

verify_token = secrets.token_urlsafe(16)
print(verify_token)
