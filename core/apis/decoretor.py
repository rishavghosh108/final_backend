from functools import wraps
from flask import request
import os
from core.libs.assertions import assert_found

def accept_payload(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        incoming_payload = request.json
        return func(incoming_payload, *args, **kwargs)
    return wrapper

def verification_payload(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token=request.headers.get(os.getenv('otp_verify_header_key'))
        assert_found(token,"verification token is missing !")
        return func(token, *args, **kwargs)
    return wrapper

def authorization_payload(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token=request.headers.get(os.getenv('authorization_header_key'))
        assert_found(token, "Authorization token is missing")
        return func(token, *args, **kwargs)
    return wrapper