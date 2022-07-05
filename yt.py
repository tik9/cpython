
import youtube_dl
from youtubesearchpython import VideosSearch
import webbrowser

# search_v = 'calma'
search_v = 'paso de la luna'
# search_v = 'penny lane'


def main():
    vid = search()
    # dl(vid)
    # print(vid)
    webbrowser.open(vid)


def search():
    videosSearch = VideosSearch(search_v, limit=1)
    return videosSearch.result()['result'][0]['link']


def dl(vid):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([vid])


if __name__ == '__main__':
    main()
