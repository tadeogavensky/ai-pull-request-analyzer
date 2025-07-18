from fastapi import FastAPI
from starlette.responses import RedirectResponse
from dotenv import load_dotenv
import os
import httpx

load_dotenv()

app = FastAPI()

GITHUB_CLIENT_ID = os.environ["GITHUB_CLIENT_ID"]
GITHUB_CLIENT_SECRET = os.environ["GITHUB_CLIENT_SECRET"]


@app.get("/login")
async def github_login():
    return RedirectResponse(
        f"https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}",
        status_code=302,
    )


@app.get("/callback")
async def callback(code: str):
    params = {
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "code": code,
    }
    headers = {'Accept': 'application/json'}
    async with httpx.AsyncClient() as client:
        response = await client.post(url="https://github.com/login/oauth/access_token", params=params, headers=headers)
        
    response_json = response.json()
    access_token = response_json['access_token']
    async with httpx.AsyncClient() as client:
        headers.update({'Authorization': f'Bearer {access_token}'})
        response = await client.get('https://api.github.com/user', headers=headers )
        
    return response.json()
    
