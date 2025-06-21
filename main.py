from fastapi import FastAPI, Request
import requests

app = FastAPI()

CLIENT_ID = "DS3ERW52MY-100"  # Replace with your real Client ID
SECRET_KEY = "GGBAOXEV1I"  # Replace with your real Secret Key
REDIRECT_URI = "https://fyers-fastapi-api.onrender.com/callback"

@app.get("/")
def home():
    return {"message": "Welcome to FYERS FastAPI Bot"}

@app.get("/generate-auth-url")
def generate_auth_url():
    url = (
        f"https://api-t1.fyers.in/api/v3/generate-authcode"
        f"?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code"
    )
    return {"auth_url": url}

@app.get("/callback")
def callback(request: Request):
    auth_code = request.query_params.get("auth_code")

    if not auth_code:
        return {"error": "Authorization code not found in query parameters."}

    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "secret_key": SECRET_KEY,
        "code": auth_code,
        "redirect_uri": REDIRECT_URI
    }

    response = requests.post("https://api.fyers.in/api/v3/token", json=payload)
    return response.json()
