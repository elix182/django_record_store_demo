from django.urls import path
from . import views

app_name = 'records'
urlpatterns = [
    path('', views.index, name='index'),
    path('artists', views.artists, name='record'),
    path('artists/<int:record_id>', views.artist_detail, name='record_details'),
    path('release', views.record, name='record'),
    path('release/<int:record_id>', views.record_detail, name='record_details'),
    path('songs', views.songs, name='songs'),
    path('songs/<int:song_id>', views.song_detail, name='song_details'),
]