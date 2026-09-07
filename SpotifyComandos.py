import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

auth_manager = SpotifyOAuth( //add your own informations
    client_id="",
    client_secret="",
    redirect_uri="",
    scope=""
)

token_info = auth_manager.get_cached_token()
if auth_manager.is_token_expired(token_info):
    print("Token expirado. Renovando...")
    token_info = auth_manager.refresh_access_token(token_info['refresh_token'])

sp = spotipy.Spotify(auth=token_info['access_token'])

def tocar_playlist_por_emocao(emocao):
    playlists = {
        "happy": "(redicreciona para playlist)",
        "sad": "",
        "neutral": ""
    }

    playlist_uri = playlists.get(emocao)
    if not playlist_uri:
        print("Emoção não mapeada para playlist:", emocao)
        return None

    try:
        playback = sp.current_playback()

        if not playback or not playback.get('device'):
            print("Nenhum player ativo. Abra o Spotify em um dispositivo e inicie uma música manualmente.")
            return None

        sp.shuffle(state=True)
        time.sleep(1)

        sp.start_playback(context_uri=playlist_uri)
        print("Tocando playlist para emoção:", emocao)

        time.sleep(2)
        playback = sp.current_playback()
        if playback and playback["item"]:
            duration_ms = playback["item"]["duration_ms"]
            duration_sec = int(duration_ms / 1000)
            print(f"Tocando agora: {playback['item']['name']} ({duration_sec} segundos)")
            return duration_sec
        else:
            print("Nenhuma música em reprodução.")
            return 120 

    except Exception as e:
        print("Erro ao tocar playlist:", e)
        return None
