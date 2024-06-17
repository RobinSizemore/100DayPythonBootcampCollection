import requests
import datetime as dt
from bs4 import BeautifulSoup
import lxml
import spotipy
import os
import dotenv
from spotipy.oauth2 import SpotifyOAuth

dotenv.load_dotenv()

# Load Spotify credentials from environment variables
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

datestr = "1996-09-29"
is_valid_date = False

while not is_valid_date:
    datestr = input("Please enter the date you'd like to check in YYYY-mm-dd format: ")
    try:
        is_valid_date = bool(dt.datetime.strptime(datestr, "%Y-%m-%d"))
    except ValueError:
        is_valid_date = False


billboard_url = f"https://www.billboard.com/charts/hot-100/{datestr}"
response = requests.get(url=billboard_url)
soup = BeautifulSoup(response.text, "lxml")
divs = soup.find_all(name="div", class_="o-chart-results-list-row-container")
songs = []
for div in divs:
    title = div.find(name="h3", class_="c-title").text.strip()
    artist = div.find(name="h3", class_="c-title").find_next_sibling("span").text.strip()
    songs.append({"title": title, "artist": artist})


# Authenticate with Spotify
auth_manager = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri="http://example.com", scope="playlist-modify-private")
sp = spotipy.Spotify(auth_manager=auth_manager)

# Get current user's username
username = sp.current_user()["id"]

# Create a new playlist
playlist = sp.user_playlist_create(user=username, name=f"Hot Songs - {datestr}", public=False)

# Search for the Spotify URIs of the songs
uris = []
for song in songs:
    result = sp.search(q=f"track:{song['title']} artist:{song['artist']}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uris.append(uri)
    except IndexError:
        print(f"Song {song['title']} by {song['artist']} not found on Spotify.")

# Add songs to the playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=uris)
print(f"Playlist URL {playlist['external_urls']['spotify']}")
