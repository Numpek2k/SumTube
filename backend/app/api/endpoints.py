from fastapi import APIRouter, HTTPException
from app.core.youtube import get_video_id, fetch_youtube_transcript, download_audio_from_youtube
from app.core.transcription import audio_to_text
from app.core.summarization import summarize_text
from app.core.tts import text_to_speech


router = APIRouter()


@router.post("/summarize/")
async def summarize_youtube_video(youtube_url: str):
    audio_file_path = "./audio.mp3"
    video_id = get_video_id(youtube_url)
    if not video_id:
        raise HTTPException(status_code=400, detail="Invalid YouTube URL")

    transcript = fetch_youtube_transcript(video_id)
    if not transcript:
        download_audio_from_youtube(youtube_url)
        transcript = audio_to_text(audio_file_path)

    summary = summarize_text(transcript)
    audio_content = text_to_speech(summary)

    return {"summarize": summary, "transcription": transcript, "tts_audio_url": audio_content}
