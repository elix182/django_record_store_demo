from django.urls import path
from . import views

app_name = 'records'
urlpatterns = [
    # path('', views.record, name='index'),
    path('artists', views.artists, name='artists'),
    path('artists/<int:artist_id>', views.artist_detail, name='artist_details'),
    path('artists/create', views.create_artist, name='create_artist'),
    path('artists/edit/<int:artist_id>', views.edit_artist, name='edit_artist'),
    path('release', views.record, name='record'),
    path('release/<int:record_id>', views.record_detail, name='record_details'),
    path('release/create', views.record_detail, name='record_create'),
    path('songs', views.songs, name='songs'),
    path('songs/<int:song_id>', views.song_detail, name='song_details'),
]