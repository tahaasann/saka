import yt_dlp

from saka.models import Video


def fetch_playlist(url: str) -> list[Video]:
    """
    Fetch all available videos in a Youtube playlist.
    """
    with yt_dlp.YoutubeDL({"extract_flat": True, "quiet": True}) as ydl:
        info = ydl.extract_info(url, download=False)

    entries = info.get("entries")

    if entries is None:
        raise ValueError("URL is not a playlist")

    videos: list[Video] = []

    for entry in entries:
        video_id = entry.get("id")
        video_title = entry.get("title")
        video_channel = entry.get("channel")
        video_channel_id = entry.get("channel_id")
        if not video_id or not video_title or not video_channel or not video_channel_id:
            continue

        video = Video(
            id=video_id,
            title=video_title,
            duration=entry.get("duration"),
            channel=video_channel,
            channel_id=video_channel_id,
        )
        videos.append(video)

    return videos
