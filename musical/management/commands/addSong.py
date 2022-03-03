"""
Manager script to add song

To run this python file : 
    python manage.py addSong <song_name> <band_name> <album_name> <genre>
        song_name (str) : name of the song you want to add
        band_name (str) : name of the band of the song you want to add
        album_name (str) : name of the album of the song you want to add
        genre (str) : genre of the song you want to add
"""

from django.core.management.base import BaseCommand
from django.db.models import Q
from basics.models import Song

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("song_name", type=str, help="name of the song you want to add")
        parser.add_argument("band_name", type=str, help="name of the band of the song you want to add")
        parser.add_argument("album_name", type=str, help="name of the album of the song you want to add")
        parser.add_argument("genre", type=str, help="genre of the song you want to add")
    #
    def handle(self, *args, **kwargs):
        songName = kwargs["song_name"]
        albumName = kwargs["album_name"]
        bandName = kwargs["band_name"]
        genre = kwargs["genre"]
        #
        songInstance = Song.objects.filter(Q(name=songName) & Q(band=bandName) & Q(album=albumName) & Q(genre=genre)).exists()
        if songInstance:
            self.stdout.write(self.style.WARNING("Song could not added because it is already exists"))
        else:
            newSong = Song(name=songName, band=bandName, album=albumName, genre=genre)
            print(newSong)
            newSong.save()
            self.stdout.write(self.style.SUCCESS('new song created successfuly!'))