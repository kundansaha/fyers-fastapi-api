# FYERS FastAPI Integration

This FastAPI app connects to the FYERS trading API and helps generate access tokens via OAuth.

## How to Use

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the server:
   ```
   uvicorn main:app --reload
   ```

3. Visit `/generate-auth-url` to log in and get `auth_code`.

4. Visit `/callback?auth_code=xyz123` to receive your access and refresh token.

Make sure to set your credentials in the `.env` file.
