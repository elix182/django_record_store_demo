from django.db import models

class ArtistType(models.Model):
    name = models.CharField(max_length=10)

class RecordType(models.Model):
    name = models.CharField(max_length=10)

class Artist(models.Model):
    name = models.CharField(max_length=320)
    founding_date = models.DateField('date of founding')
    origin_country = models.CharField(max_length=20)
    members = models.CharField(max_length=256, null=True)
    artist_type = models.ForeignKey(ArtistType, on_delete=models.CASCADE)

class Record(models.Model):
    name = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')
    lenght_seconds = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    record_type = models.ForeignKey(RecordType, on_delete=models.CASCADE)

class Song(models.Model):
    name = models.CharField(max_length=256)
    artists = models.ManyToManyField(Artist)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    composer = models.CharField(max_length=128)
    lyrics = models.TextField(null=True)