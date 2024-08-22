# app/core/youtube.py

from pytubefix import YouTube
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
from urllib.parse import urlparse, parse_qs
from urllib.error import HTTPError

def get_video_id(youtube_url):
    query = urlparse(youtube_url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    elif query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            return parse_qs(query.query)['v'][0]
    return None

def fetch_youtube_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([item['text'] for item in transcript]).replace('\n', ' ')
    except (NoTranscriptFound, TranscriptsDisabled):
        return None

def download_audio_from_youtube(video_url):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()
        if stream is None:
            raise Exception("No audio stream available")
        output_file = stream.download('./', filename='audio.mp3')
        return output_file
    except HTTPError as e:
        print(f"HTTPError: {e.code} - {e.reason}")
        raise Exception("Failed to download video. Please check the URL or video restrictions.")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise Exception("An error occurred while downloading the audio.")
