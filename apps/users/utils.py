import random
import re
from django.core.cache import cache
from rest_framework import status
from rest_framework.exceptions import ValidationError


def get_login_data(email: str):
    return f"login:{email}"


def send_code(email: str, code: int, expired_time=300):
    print(f'Email: {email} == Code: {code}')
    _email = get_login_data(email)
    cache.set(_email, code, timeout=expired_time)


def check_email(email: str, code: int):
    _email = get_login_data(email)
    _code = cache.get(_email)
    if _code is None:
        raise ValidationError('Invalid or expired email code', status.HTTP_404_NOT_FOUND)
    print(code, _code)
    return _code == code
