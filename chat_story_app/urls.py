from django.urls import path
from .views import ChatView, download_story, HomeView
urlpatterns = [
    
    path('', HomeView.as_view(), name='home_view'),
    path('story', ChatView.as_view(), name='chat_view'),
    path('download-story', download_story, name='download_story_view'),
]
