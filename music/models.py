from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=100)
    album_title = models.CharField(max_length=150)
    album_logo = models.FileField()
    genre = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse("music:detail",kwargs={"pk":self.pk})

    def __str__(self):
        return self.artist+" - "+self.album_title


class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=20)
    song_title=models.CharField(max_length=200)
    uploaded_file=models.FileField()

    def get_absolute_url(self):

        return reverse("music:detail",kwargs={"pk":self.album.pk})

    def __str__(self):
        return "Song: "+self.song_title

