from django.urls import path
from main.views import *

urlpatterns = [
    path('create-post/', CreatePostView.as_view(), name='create_post'),
    path('create-audio/', CreateAudioPostView.as_view(), name='create_audio'),
    path('home/', HomeView.as_view(), name='home'),
]