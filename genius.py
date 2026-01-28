
import api_key
import lyricsgenius

def main():
    client_access_token = api_key.client_access_token
    LyricsGenius = lyricsgenius.Genius(client_access_token)

    artist = LyricsGenius.search_artist("sia", max_songs=2)
    song = LyricsGenius.search_song("sia", "beautiful people")
    print(song.lyrics)

    # for song in artist.songs:
        # print(song.lyrics)

if __name__ == "__main__":
    main()
