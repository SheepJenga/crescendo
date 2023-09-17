from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = SPOTIFY_CLIENT_ID + ":" + SPOTIFY_CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded" # normally json or some shit? idk youtube video
    }
    data = {"grant_type": "client_credentials"}

    result = post(url, headers=headers, data=data) # returning some json data
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_artist_id(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1" # first artist pops up # query = f"q={artist_name}&type=artist,track"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['artists']['items']

    if len(json_result) == 0:
        return None

    return json_result[0]['id']

def search_for_song_id(token, artist_name, song_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={song_name}&type=track"
    query_url = url+query

    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)['tracks']['items']

    if len(json_result) == 0:
        return None

    query_artist = search_for_artist_id(token, artist_name)
    for track in json_result:
        artist_id = track['artists'][0]['id']
        if artist_id == query_artist:
            return track['id']
    return None

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)

    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

def get_song_by_id(token, track_id):
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = get_auth_header(token)

    result = get(url, headers=headers)
    json_result = json.loads(result.content)
    return json_result

if __name__ == "__main__":
    token = get_token()
    # artist = search_for_artist_id(token, 'The_Chainsmokers')

    # artist_id = artist
    # songs = get_songs_by_artist(token, artist_id)

    song = search_for_song_id(token, 'The_Chainsmokers', 'Paris')

    track = get_song_by_id(token, song)
    print(track)