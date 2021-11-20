from datetime import datetime

from background_task import background
from django.conf import settings
from googleapiclient.discovery import build

from .models import Video


@background(schedule=1)
def fetch_api():
    Video.objects.all().delete()
    youtube = build("youtube", "v3", developerKey=settings.YOUTUBE_API_KEY)
    req = youtube.search().list(
        q="football", part="snippet", type="video", maxResults=100
    )
    res = req.execute()["items"]
    for data in res:
        try:
            thumbnail = data["snippet"]["thumbnails"]["medium"]["url"]
        except KeyError:
            thumbnail = data["snippet"]["thumbnails"]["high"]["url"]

        Video.objects.create(
            url="https://youtu.be/" + data["id"]["videoId"],
            title=data["snippet"]["title"],
            description=data["snippet"]["description"],
            thumbnail=thumbnail,
            datetime=datetime.fromisoformat(data["snippet"]["publishedAt"][:-1]),
        )
