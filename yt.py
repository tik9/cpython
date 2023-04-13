'''Youtube viewer with videos from a video file list'''

import webbrowser
import youtube_dl
from youtubesearchpython import VideosSearch
from pprint import pprint

with open('videolist', encoding='utf-8') as vid:
    all_vids = vid.read().splitlines()
    last = all_vids[-1]


def main():
    '''main'''
    video = search()
    # download(video)
    # pprint(sorted(all_vids))
    webbrowser.open(video)


def search():
    '''search'''
    return VideosSearch(last, limit=1).result()['result'][0]['link']


def download(vid):
    '''download video'''
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
