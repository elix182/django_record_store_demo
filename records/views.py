from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

# =========== Artist ===========

def artists(request):
  artists_list = Artist.objects.all()
  context = {'artists_list': artists_list}
  return render(request, 'artists/index.html', context)

def artist_detail(request, artist_id):
  artist = get_object_or_404(Artist, pk=artist_id)
  context = {'artist': artist}
  return render(request, 'artists/detail.html', context)

def create_artist(request, artist_id):
  return render(request, 'artists/create.html')

def edit_artist(request, artist_id):
  artist = get_object_or_404(Artist, pk=artist_id)
  context = {'artist': artist}
  return render(request, 'artists/edit.html', context)

def create_artist_request(request):
  name = request.POST['name']
  founding_date = request.POST['founding_date']
  origin_country = request.POST['origin_country']
  members = request.POST['members']
  artist_type = ArtistType.objects.get(request.POST['artist_type'])
  artist = Record(name=name, founding_date=founding_date, origin_country=origin_country,
   members=members)
  artist.type = artist_type
  artist.save()
  return HttpResponseRedirect(reverse('records:artists'))

def update_artist_request(request, artist_id):
  artist = get_object_or_404(Artist, pk=artist_id)
  name = request.POST['name']
  founding_date = request.POST['founding_date']
  origin_country = request.POST['origin_country']
  members = request.POST['members']
  artist_type = ArtistType.objects.get(request.POST['artist_type'])
  artist.name = name
  artist.founding_date = founding_date
  artist.origin_country = origin_country
  artist.members = members
  artist.type = artist_type
  artist.save()
  return HttpResponseRedirect(reverse('records:artists'))

def delete_artist_request(request, artist_id):
  artist = get_object_or_404(Artist, pk=artist_id)
  artist.delete()
  return HttpResponseRedirect(reverse('records:artists'))

# ============== RECORD ===========

def record(request):
  records_list = Record.objects.all()
  context = {'records_list': records_list}
  return render(request, 'records/index.html', context)

def record_detail(request, record_id):
  record = get_object_or_404(Record, pk=record_id)
  context = {'record': record}
  return render(request, 'records/detail.html', context)

def create_record_request(request):
  name = request.POST['name']
  pub_date = request.POST['pub_date']
  length_seconds = request.POST['lenght_seconds']
  artist = Artist.objects.get(pk=request.POST['artist'])
  record_type = RecordType.objects.get(request.POST['record_type'])
  record = Record(name=name, pub_date=pub_date, length_seconds=length_seconds)
  record.artist = artist
  record.record_type = record_type
  record.save()
  return HttpResponseRedirect(reverse('records:record'))

# =========== Songs ===========

def songs(request):
  songs_list = Song.objects.all()
  context = {'songs_list': songs_list}
  return render(request, 'songs/index.html', context)

def song_detail(request, song_id):
  song = get_object_or_404(Song, pk=song_id)
  context = {'song': song}
  return render(request, 'songs/detail.html', context)
