'''Youtube viewer'''

import webbrowser
import youtube_dl
from youtubesearchpython import VideosSearch
from os.path import join, dirname

with open(join(dirname(__file__), 'vids'), 'r', encoding='utf-8') as vid:
    last = vid.read().splitlines()[-1]


def main():
    '''main'''
    vid = search()
    # print(vid)
    webbrowser.open(vid)


def search():
    '''search'''
    return VideosSearch(last, limit=1).result()['result'][0]['link']


def download(vid):
    '''download YT vid'''
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
