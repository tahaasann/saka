from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Video:
    id: str
    title: str
    duration: int | None
    channel: str
    channel_id: str
