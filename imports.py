import asyncio
import base64
import glob
from datetime import datetime

import httpx
import pandas as pd

#class ebayApi():
    #def __init__ (self, apiKey):

def load_csv():
    files = glob.glob('./inputs/*.csv')
    df_list = []

    for f in files:
        csv = pd.read_csv(f, dtype={'upc': 'str'})
        df_list.append(csv)

    if len(df_list) == 0:
        raise Exception("No csv file found in the inputs folder.")
    data = pd.concat(df_list)
    print("yes")
    print(data)
    return data.to_dict("records")


async def get_ebay_auth_token(client_id, client_secret):
    time = datetime.now()

    async def log_request(request):
        print(f"{time}: Request event hook: {request.method} {request.url} - Waiting for response")

    async def log_response(response):
        request = response.request
        print(f"{time}: Response event hook: {request.method} {request.url} - Status {response.status_code}")

    async with httpx.AsyncClient(event_hooks={'request': [log_request], 'response': [log_response]}) as client:
        url = "https://api.ebay.com/identity/v1/oauth2/token"
        credentials = f"{client_id}:{client_secret}"
        encoded_credentials = base64.b64encode(credentials.encode('utf-8')).decode('utf-8')
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {encoded_credentials}"
        }
        body = {
            "grant_type": "client_credentials",
            "scope": "https://api.ebay.com/oauth/api_scope"
        }
        response = await client.post(url, headers=headers, data=body)

        if response.status_code == 200:
            return response.json().get("access_token")
        else:
            print("Failed to obtain token:", response.text)
            return None
