from django.urls import path
from . import views

app_name = 'records'
urlpatterns = [
    # path('', views.record, name='index'),
    path('artists', views.artists, name='artists'),
    path('artists/<int:artist_id>', views.artist_detail, name='artist_details'),
    path('artists/register', views.create_artist, name='create_artist'),
    path('artists/edit/<int:artist_id>', views.edit_artist, name='edit_artist'),
    path('artists/create', views.create_artist_request, name='create_artist_request'),
    path('artists/update/<int:artist_id>', views.update_artist_request, name='update_artist_request'),
    path('artists/delete/<int:artist_id>', views.delete_artist_request, name='delete_artist_request'),
    path('release', views.record, name='record'),
    path('release/<int:record_id>', views.record_detail, name='record_details'),
    path('release/register', views.create_record, name='create_record'),
    path('release/edit/<int:record_id>', views.edit_artist, name='edit_record'),
    path('songs', views.songs, name='songs'),
    path('songs/<int:song_id>', views.song_detail, name='song_details'),

    #Pseudo-REST stuff
    path('artisttype', views.get_artist_type),
    path('recordtype', views.get_record_type),
]