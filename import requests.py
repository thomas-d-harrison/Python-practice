import requests

def get_spotify_access_token(client_id, client_secret):
    auth_url = "https://accounts.spotify.com/api/token"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    }
    response = requests.post(auth_url, headers=headers, data=data)
    access_token = response.json().get('access_token')
    return access_token

def get_beyonce_top_tracks(access_token):
    url = "https://api.spotify.com/v1/artists/6vWDO969PvNqNYHIOW5v0m/top-tracks"
    params = {'country': 'US'}  # Specify the country to get top tracks in that region
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    CLIENT_ID = 'your_client_id_here'
    CLIENT_SECRET = 'your_client_secret_here'

    access_token = get_spotify_access_token(CLIENT_ID, CLIENT_SECRET)
    if access_token:
        beyonce_top_tracks = get_beyonce_top_tracks(access_token)
        if beyonce_top_tracks:
            print(beyonce_top_tracks)
        else:
            print("Failed to get Beyoncé's top tracks.")
    else:
        print("Failed to authenticate with Spotify.")
