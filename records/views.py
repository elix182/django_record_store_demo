from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *

def index(request):
  return HttpResponse("Nice record store view")

def artists(request):
  return HttpResponse("You're looking at artists index.")

def artist_detail(request, artist_id):
  return HttpResponse("You're looking at artist %s." % artist_id)

def create_artist(request):
  name = request.POST['name']
  founding_date = request.POST['founding_date']
  origin_country = request.POST['origin_country']
  members = request.POST['members']
  artist_type = ArtistType.objects.get(request.POST['artist_type'])
  artist = Record(name=name, founding_date=founding_date, origin_country=origin_country, members=members)
  artist.type = artist_type
  artist.save()
  return HttpResponseRedirect(reverse('polls:results'))

def record(request):
  records_list = Record.objects.all()
  context = {'records_list': records_list}
  return render(request, 'records/index.html', context)

def record_detail(request, record_id):
  record = get_object_or_404(Record, pk=record_id)
  context = {'record': record}
  return render(request, 'records/detail.html', context)

def create_record(request):
  name = request.POST['name']
  pub_date = request.POST['pub_date']
  length_seconds = request.POST['lenght_seconds']
  artist = Artist.objects.get(pk=request.POST['artist'])
  record_type = RecordType.objects.get(request.POST['record_type'])
  record = Record(name=name, pub_date=pub_date, length_seconds=length_seconds)
  record.artist = artist
  record.record_type = record_type
  record.save()
  return HttpResponseRedirect(reverse('polls:results'))

def songs(request):
    response = "You're looking at the songs index."
    return HttpResponse(response)

def song_detail(request, song_id):
    response = "You're looking at the details of the song %s."
    return HttpResponse(response % song_id)