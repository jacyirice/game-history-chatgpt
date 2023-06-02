from django.urls import path
from .views import chat_view, download_story, home_view

urlpatterns = [
    path('', home_view, name='home_view'),
    path('story', chat_view, name='chat_view'),
    path('download-story', download_story, name='download_story_view'),
]
