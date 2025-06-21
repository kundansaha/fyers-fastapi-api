from fastapi import FastAPI, Request
import requests

app = FastAPI()

CLIENT_ID = "DS3ERW52MY-100"  # Replace with your actual App ID
SECRET_KEY = "YOUR_SECRET_KEY"  # Replace with your actual app secret key
REDIRECT_URI = "https://fyers-fastapi-api.onrender.com/callback"

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
