from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    views = models.CharField(max_length=20)
    datetime = models.DateTimeField()
    url = models.URLField()
    thumbnail = models.URLField()
    description = models.TextField()
