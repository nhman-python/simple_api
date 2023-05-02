import string
from fastapi import FastAPI, Request, Header
import secrets

app = FastAPI()


@app.get('/')
async def root(request: Request, length: int = Header('length')):
    password = 'No password generated'
    length = request.headers.get('length', None)
    if length is not None and length.isdigit():
        if 0 < int(length) < 100+1:
            password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(int(length)))
    return {'random_password': password, 'test': 'text'}

