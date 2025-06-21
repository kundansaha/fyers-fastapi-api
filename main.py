from fastapi import FastAPI
from fyers_auth import get_auth_url, get_access_token

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FYERS FastAPI Bot"}

@app.get("/generate-auth-url")
def auth_url():
    return {"auth_url": get_auth_url()}

@app.get("/callback")
def callback(auth_code: str):
    token = get_access_token(auth_code)
    return token
