from django.views import generic
from music.models import Album,Song
from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy,reverse


class IndexView(generic.ListView):
    template_name = "music/index.html"
    context_object_name = "album_data"

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = "music/detail.html"

def all_songs(request):
    songs=Song.objects.all()
    return render(request, "music/all_songs.html",{"songs":songs} )



class CreateAlbum(CreateView):
    model = Album
    fields = ["artist","album_title","album_logo","genre"]


class UpdateAlbum(UpdateView):
    model = Album
    fields = ["artist","album_title","album_logo","genre"]


class DeleteAlbum(DeleteView):
    model = Album
    success_url = reverse_lazy("music:index")


class CreateSong(CreateView):
    model = Song
    fields = ['album','file_type',"song_title","uploaded_file"]

class DeleteSong(DeleteView):
    model = Song
    success_url = reverse_lazy("music:index")


