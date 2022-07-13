from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from pprint import pprint
from app.dict_raperos import artistas_dict1

MAX_RESULTS = 5
author = 'Tino el'
id_aleman = '4QFG9KrGWEbr6hNA58CAqE'
artistas_result1 = {}
id_aczino = '4r1ZDYKzPt3iIjuq8LbT6X'

def get_client():
    
    client_id = '5b0c6adf9d764c30bcf055369080e7a4'
    client_secret = '81fa5a3f1419487e8987b67af94f97f0'
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
    return sp 
    
def get_top_100():
    sp_client = get_client()
    for artista in artistas_dict1:
        artista = sp_client.artist(artista[id])
        artistas_result1[artista['name']] = artista['followers']['total']
    top = dict(sorted(artistas_result1.items(), key=lambda item: item[1], reverse=True))
    lista = top.items()
    top100 = list(lista)[:100]
    return top100
    
def get_top_track_for_artist(artist: str):
    sp_client = get_client()
    result = sp_client.artist_top_tracks(artist)
    for track in result['tracks'][:11]:
        pprint(track['name'])