from fyers_apiv3 import fyersModel
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("FYERS_CLIENT_ID")
secret_key = os.getenv("FYERS_SECRET_KEY")
redirect_uri = os.getenv("FYERS_REDIRECT_URI")

session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type="code"
)

def get_auth_url():
    return session.generate_authcode()

def get_access_token(auth_code: str):
    session.set_token(auth_code)
    response = session.generate_token()
    return response
