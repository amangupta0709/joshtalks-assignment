# from django.conf import settings
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render
from httplib2 import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Video
from .serialize import VideoSerializer


class VideoList(APIView, PageNumberPagination):
    def get(self, request):
        query = self.request.query_params.get("q")
        if query:
            videos = (
                Video.objects.annotate(search=SearchVector("title", "description"))
                .filter(search=query)
                .order_by("datetime")
            )
        else:
            videos = Video.objects.all().order_by("datetime")

        page = self.paginate_queryset(videos, request, view=self)
        serializer = VideoSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)
