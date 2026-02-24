#this is the main file for codeing
from fastapi import FastAPI
from datetime import datetime, timedelta
from jose import jwt
from pydantic import BaseModel
app = FastAPI()

class Crendentials(BaseModel):
    username: str
    password: str

users = {
    'mepatilyogesh':{'pwd': '1234', 'role': 'user'}
}

sercret_key = 'acef7609cc1f561ff7e51415fa0b1cba2086e8cbbc4a49ef46eb076b58f35ae4'
ALGO = 'HS256'

def create_token(username, role):
    payload = {
        "sub": username,
        "role": role,
        "exp": datetime.utcnow() + timedelta(minutes=10)
        }

    return jwt.encode(payload, sercret_key, algorithm=ALGO)


@app.post('/login')
def user_login(payload: Crendentials):
    if payload.username in users and users[payload.username]['pwd'] == payload.password:
        token = create_token(payload.username, users[payload.username]['role'])
        return {"access_token": token, 'token_type': "bearer"}

