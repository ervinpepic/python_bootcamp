import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup


SPOTIFY_CLIENT_ID = ""
SPOTIFY_CLIENT_SECRET = ""
SPOTIPY_REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"
CACHE = '.spotipyoauthcache'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID, 
        client_secret=SPOTIFY_CLIENT_SECRET, 
        scope=SCOPE, 
        redirect_uri=SPOTIPY_REDIRECT_URI,
        show_dialog=True,
        cache_path="token.txt"
        ))
user_id = sp.current_user()["id"]
print(user_id)

date_input = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD ")
SONGS_URL = f"https://www.billboard.com/charts/hot-100/{date_input}"

response = requests.get(SONGS_URL)
html_data = response.text
soup = BeautifulSoup(html_data, "html.parser")
song_tags = soup.find_all(name="h3", class_=['c-title ', 'a-no-trucate'])
songs_list = [song.getText().strip() for song in song_tags]

song_uris = []
year = date_input.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)