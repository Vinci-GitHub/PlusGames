import jwt
import datetime
from django.conf import settings




# コメント
def generate_access_token(accounts):
    payload = {
        'accounts_id': accounts.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')