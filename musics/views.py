from django.shortcuts import render, redirect

from common.session_decorator import session_decorator
from musicApp.settings import session
from musics.forms import AlbumCreateForm, AlbumEditForm
from musics.models import Album


@session_decorator(session)
def index(request):
    albums = session.query(Album).all()

    context = {
        'albums': albums,
    }

    return render(request, 'common/index.html', context)


@session_decorator(session)
def create_album(request):
    if request.method == 'GET':

        context = {
            'form': AlbumCreateForm(),
        }

        return render(request, 'albums/create-album.html', context)

    elif request.method == 'POST':
        form = AlbumCreateForm(request.POST)

        if form.is_valid():
            new_album = Album(
                album_name=form.cleaned_data['album_name'],
                image_url=form.cleaned_data['image_url'],
                price=form.cleaned_data['price'],
            )

            session.add(new_album)

        return redirect('index')


@session_decorator(session)
def details_album(request, id):
    album = session.query(Album).filter(Album.id == id).first()

    context = {
        'album': album,
    }
    return render(request, 'albums/album-details.html', context)


@session_decorator(session)
def edit_album(request, id):
    album = session.query(Album).filter(Album.id == id).first()

    if request.method == "GET":
        initial_data = {
            'album_name': album.album_name,
            'image_url': album.image_url,
            'price': album.price,
        }

        form = AlbumEditForm(initial=initial_data)

        context = {
            'form': form,
            'album': album,
        }

        return render(request, 'albums/edit-album.html', context)

    elif request.method == "POST":
        form = AlbumEditForm(request.POST)

        if form.is_valid():
            album.album_name = form.cleaned_data['album_name']
            album.image_url = form.cleaned_data['image_url']
            album.price = form.cleaned_data['price']

        return redirect('index')


def delete_album(request, id):
    return render(request, 'albums/delete-album.html')


def create_song(request):
    return render(request, 'songs/create-song.html')
