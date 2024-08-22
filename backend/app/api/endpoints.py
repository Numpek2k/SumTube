from fastapi import APIRouter, HTTPException
from app.core.youtube import get_video_id, fetch_youtube_transcript, download_audio_from_youtube
from app.core.transcription import audio_to_text
from app.core.summarization import summarize_text
from app.core.tts import text_to_speech


router = APIRouter()


# @router.post("/summarize/")
# async def summarize_youtube_video(youtube_url: str, voice_name: str = "en-US-Wavenet-D"):
#     video_id = get_video_id(youtube_url)
#     if not video_id:
#         raise HTTPException(status_code=400, detail="Invalid YouTube URL")
#
#     transcript = fetch_youtube_transcript(video_id)
#     if not transcript:
#         audio_file = download_audio_from_youtube(youtube_url)
#         transcript = audio_to_text(audio_file)
#
#     summary = summarize_text(transcript)
#     audio_content = text_to_speech(summary, voice_name)
#
#     return {"summary": summary, "audio": audio_content}


@router.get("/video_inf/")
async def video_inf():
    youtube_url_en_trasciption = 'https://www.youtube.com/watch?v=O9pD6LTF4Bk'
    youtube_url_pl_not_transcripted = 'https://www.youtube.com/watch?v=GSv5tntgEnM'
    video_id = get_video_id(youtube_url_en_trasciption)
    if not video_id:
        raise HTTPException(status_code=400, detail="Invalid YouTube URL")

    transcript = fetch_youtube_transcript(video_id)
    # transcript = 'The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct. The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the ta'
    if not transcript:
        audio_file = download_audio_from_youtube(youtube_url_en_trasciption)
        # transcript = audio_to_text(audio_file)

    summary = summarize_text(transcript)
    # audio_content = text_to_speech(summary, voice_name)

    return {"summarize": summary ,"transcription": transcript}