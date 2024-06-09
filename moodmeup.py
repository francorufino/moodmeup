# import base64
# import requests
# import subprocess
# from dotenv import load_dotenv
# import os

# # Carregar variáveis do arquivo .env
# load_dotenv()

# client_id = os.getenv("CLIENT_ID")
# client_secret = os.getenv("CLIENT_SECRET")

# def notify_user(message):
#     subprocess.run(["osascript", "-e", f'display notification "{message}" with title "Spotify API Notification"'])

# def get_token(client_id, client_secret):
#     base64_auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

#     auth_options = {
#         'url': 'https://accounts.spotify.com/api/token',
#         'headers': {
#             'Authorization': 'Basic ' + base64_auth,
#             'Content-Type': 'application/x-www-form-urlencoded'
#         },
#         'data': {
#             'grant_type': 'client_credentials'
#         }
#     }

#     response = requests.post(auth_options['url'], headers=auth_options['headers'], data=auth_options['data'])

#     if response.status_code == 200:
#         r = response.json()
#         token = r['access_token']
#         token_type = r['token_type']
#         token_duration = r['expires_in']
#         print(f'Token de Acesso requisitado com sucesso!')
#         print(f'Tipo do Token: {token_type}')
#         print(f'Disponibilidade do Token: {token_duration} segundos')
#         notify_user(f"Token obtido com sucesso! Tipo: {token_type}, Duração: {token_duration} segundos")
#     else:
#         print('Não foi possível obter o token de acesso')
#         notify_user("Falha ao obter o token de acesso")

#     return f'{token_type} {token}'

# # Chamar a função para testar
# token = get_token(client_id, client_secret)
# print(f'Token: {token}')


# working code with dataframe:
import base64
import requests
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token(client_id, client_secret):
    base64_auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()

    auth_options = {
        'url': 'https://accounts.spotify.com/api/token',
        'headers': {
            'Authorization': 'Basic ' + base64_auth,
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        'data': {
            'grant_type': 'client_credentials'
        }
    }

    response = requests.post(auth_options['url'], headers=auth_options['headers'], data=auth_options['data'])

    if response.status_code == 200:
        r = response.json()
        token = r['access_token']
        token_type = r['token_type']
        return f'{token_type} {token}'
    else:
        print('Failed to get access token')
        return None

def search_happy_playlists(token, query="happy"):
    url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": token
    }
    params = {
        "q": query,
        "type": "playlist",
        "limit": 5
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        playlists = response.json()["playlists"]["items"]
        return playlists
    else:
        print(f"Failed to search playlists: {response.status_code}")
        return []

def get_playlist_tracks(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = {
        "Authorization": token
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        tracks = response.json()["items"]
        return [track["track"]["id"] for track in tracks if track["track"]]
    else:
        print(f"Failed to get playlist tracks: {response.status_code}")
        return []

def get_audio_features(token, track_ids):
    url = f"https://api.spotify.com/v1/audio-features"
    headers = {
        "Authorization": token
    }
    params = {
        "ids": ",".join(track_ids)
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["audio_features"]
    else:
        print(f"Failed to get audio features: {response.status_code}")
        return []

def recommend_happy_tracks(audio_features):
    happy_tracks = [
        feature for feature in audio_features
        if feature["valence"] > 0.7 and feature["energy"] > 0.6 and feature["tempo"] > 100
    ]
    return happy_tracks

# Main execution
token = get_token(client_id, client_secret)
if token:
    playlists = search_happy_playlists(token)
    if playlists:
        playlist_id = playlists[0]["id"]
        track_ids = get_playlist_tracks(token, playlist_id)
        if track_ids:
            audio_features = get_audio_features(token, track_ids)
            if audio_features:
                happy_tracks = recommend_happy_tracks(audio_features)
                track_info = []
                for track in happy_tracks:
                    track_id = track["id"]
                    url = f"https://api.spotify.com/v1/tracks/{track_id}"
                    headers = {
                        "Authorization": token
                    }
                    response = requests.get(url, headers=headers)
                    if response.status_code == 200:
                        track_data = response.json()
                        track_name = track_data["name"]
                        artists = ", ".join([artist["name"] for artist in track_data["artists"]])
                        track_info.append({
                            "ID": track_id,
                            "Track": track_name,
                            "Artists": artists,
                            "Valence": track["valence"],
                            "Energy": track["energy"],
                            "Tempo": track["tempo"]
                        })

                tracks_df = pd.DataFrame(track_info)
                print(tracks_df)


