'''Youtube viewer with videos from a video file list'''

from pathlib import Path
import webbrowser
from youtubesearchpython import VideosSearch
import pprint
from pytube import YouTube
import os
from youtube_transcript_api import YouTubeTranscriptApi
import json

home=str(Path.home())

with open('ytlist') as file:
    all = file.read().splitlines()
    last = all[-1]


def main():
    '''main'''
    # video_link='a0Ri763zXR8'
    # pprint.pprint(sorted(all))
    # video=VideosSearch(last, limit=1).result()['result'][0]['link']
    # video_link=video.split("=",1)[1]
    # ts=YouTubeTranscriptApi.get_transcript(video_link)
    # print(ts)
    # with open('data.json', 'w', encoding='utf-8') as f:
        # json.dump(ts, f, ensure_ascii=False, indent=4)
    
    # download2(video)
    # webbrowser.open(video)

def download2(vid):

    yt = YouTube(vid)

    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=os.path.join(home,'Music'))

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

def download(vid):
    '''download video, for converting to audio ffmpeg needed'''
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
