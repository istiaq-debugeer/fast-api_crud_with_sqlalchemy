from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime,timedelta
from jose import jwt
outh2_schema=OAuth2PasswordBearer(tokenUrl='token')

SECRET_KEY='8y3194983740743079093yeodhdfo0dyuye3uifwir20quwe'
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=30


def create_access_token(data: dict,expires_delta:Optional[timedelta]=None):
    to_encode=data.copy()
    if expires_delta:
        expire=datetime.utcnow()+expires_delta
    else:
        expire=datetime.utcnow()+timedelta(minutes=15)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt