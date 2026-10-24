class SakaError(Exception):
    """Base exception for all pipeline-related errors in Saka."""


class TranscriptNotAvailable(SakaError):
    """Raised when transcripts are unavailable or disabled for the video."""
