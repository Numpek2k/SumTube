
# SumTube

This project is a backend service designed to take a YouTube video link, transcribe the video, summarize the content, and provide a text-to-speech (TTS) conversion of the summary. The service is exposed through a REST API with a single endpoint.

## Features

- **Transcription:** Converts the audio of the YouTube video into text.
- **Summarization:** Generates a concise summary of the transcribed text.
- **Text-to-Speech (TTS):** Converts the summary text into speech, providing an audio file of the summary.

## Usage

1. **Run the API:**

   ```bash
   uvicorn app.api.endpoints:app --host 0.0.0.0 --port 8000
   ```

2. **Send a POST request to the `/summarize/` endpoint with a YouTube video URL.**

   Example request:

   ```bash
   curl -X POST "http://localhost:8000/summarize/" -H "Content-Type: application/json" -d '{"url": "https://www.youtube.com/watch?v=example"}'
   ```

3. **Response:**
   - `transcription`: The full transcription of the video.
   - `summary`: A summarized version of the transcription.
   - `tts_audio_url`: A URL to download the audio file of the summarized text.

## API Endpoint

### `POST /summarize/`

**Request Body:**

```json
{
  "youtube_url": "string"  # YouTube video URL
}
```

**Response:**

```json
{
  "transcription": "string",   # Full transcription of the video
  "summarize": "string",         # Summarized text of the transcription
  "tts_audio_url": "string"    # URL to the TTS audio file of the summary
}
```