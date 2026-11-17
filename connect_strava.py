import os
import requests

CLIENT_ID = os.getenv("STRAVA_CLIENT_ID")
CLIENT_SECRET = os.getenv("STRAVA_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("STRAVA_REFRESH_TOKEN")

def get_access_token():
    auth_url = "https://www.strava.com/oauth/token"
    payload = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'refresh_token': REFRESH_TOKEN,
        'grant_type': 'refresh_token'
    }
    res = requests.post(auth_url, data=payload)
    access_token = res.json().get('access_token')
    return access_token

def fetch_activities():
    access_token = get_access_token()
    headers = {'Authorization': f'Bearer {access_token}'}
    activities_url = "https://www.strava.com/api/v3/athlete/activities"
    
    response = requests.get(activities_url, headers=headers, params={'per_page': 5})
    activities = response.json()
    
    print("Últimas atividades no Strava:")
    for act in activities:
        print(f"- {act['name']} ({act['distance']} metros)")

if __name__ == "__main__":
    fetch_activities()
