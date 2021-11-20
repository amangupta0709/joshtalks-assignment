from django.urls import path

from api import views

urlpatterns = [path("", views.VideoList.as_view(), name="get")]

# fetch_api(repeat=10, repeat_until=None)
