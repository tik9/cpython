
import youtube_dl
from youtubesearchpython import VideosSearch

search_v = 'paso de la luna'
# vid = 'https://www.youtube.com/watch?v=NQ3YKiMZDxw'


def main():
    vid = search()
    dl(vid)
    # print(result)


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


def search():
    videosSearch = VideosSearch(search_v, limit=5)
    return videosSearch.result()['result'][0]['link']


if __name__ == '__main__':
    main()
