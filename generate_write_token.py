import requests

url = "https://www.strava.com/oauth/token"

payload = {
    'client_id': '',
    'client_secret': '',
    'code': '',
    'grant_type': 'authorization_code'
}

response = requests.post(url, data=payload)

if response.status_status == 200:
    data = response.json()
    print("✅ Sucesso!")
    print(f"New Access Token: {data['access_token']}")
    print(f"New Refresh Token: {data['refresh_token']}")
    print(f"Expires in : {data['expires_at']}")
else:
    print("❌ Error generating token:")
    print(response.json())
