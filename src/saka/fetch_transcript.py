from youtube_transcript_api import (
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
    YouTubeTranscriptApi,
)

from saka.exceptions import TranscriptNotAvailable
from saka.models import Segment, Transcript


def fetch_transcript(video_id: str) -> Transcript:
    """Return the transcript for the given video ID.

    Raises:
        TranscriptNotAvailable: If no transcript is found, captions are disabled, or the video is unavailable (e.g., deleted or private).

    """
    youtube_api = YouTubeTranscriptApi()
    try:
        fetched_transcript = youtube_api.fetch(video_id)
    except (TranscriptsDisabled, NoTranscriptFound, VideoUnavailable) as e:
        raise TranscriptNotAvailable(
            f"No transcript available for video: '{video_id}'"
        ) from e

    total_segments: list[Segment] = []

    for snippet in fetched_transcript:
        total_segments.append(
            Segment(text=snippet.text, start=snippet.start, duration=snippet.duration)
        )

    final_transcript = Transcript(
        video_id=video_id,
        language=fetched_transcript.language_code,
        segments=tuple(total_segments),
    )

    return final_transcript
