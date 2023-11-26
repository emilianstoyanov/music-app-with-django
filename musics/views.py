from django.shortcuts import render

from common.session_decorator import session_decorator
from musicApp.settings import session
from musics.forms import AlbumCreateForm
from musics.models import Album


@session_decorator(session)
def index(request):
    albums = session.query(Album).all()

    context = {
        'albums': albums,
    }

    return render(request, 'common/index.html', context)


def create_album(request):
    if request.method == 'GET':
        context = {
            'form': AlbumCreateForm(),
        }

        return render(request, 'albums/create-album.html', context)


def details_album(request, id):
    return render(request, 'albums/album-details.html')


def edit_album(request, id):
    return render(request, 'albums/edit-album.html')


def delete_album(request, id):
    return render(request, 'albums/delete-album.html')


def create_song(request):
    return render(request, 'songs/create-song.html')
