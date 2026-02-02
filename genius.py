
import requests
import api_key
import lyricsgenius

client_access_token = api_key.client_access_token

def main():
    artist_name = "Sia"
    LyricsGenius = lyricsgenius.Genius(client_access_token)

    songs = LyricsGenius.search_artist(artist_name, max_songs=2)
    song = LyricsGenius.search_song(artist_name, "beautiful people")
    print(songs)
    print(song.lyrics)

def test(  ):
    search_term = "sia"
    genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"
    response = requests.get(genius_search_url)
    json_data = response.json()
    for song in json_data['response']['hits']:
        print(song['result']['full_title'])

if __name__ == "__main__":
    main()
