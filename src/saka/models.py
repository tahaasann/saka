from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Video:
    id: str
    title: str
    duration: int | None
    channel: str
    channel_id: str


@dataclass(frozen=True, slots=True)
class Segment:
    text: str
    start: float
    duration: float


@dataclass(frozen=True, slots=True)
class Transcript:
    video_id: str
    language: str
    segments: tuple[Segment, ...]
