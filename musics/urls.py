from django.urls import path, include
from musics import views

urlpatterns = [
    path('', views.index, name='index'),
    path('album/', include([
        path('create/', views.create_album, name='create album'),
        path('details/<int:id>/', views.details_album, name='details album'),
        path('edit/<int:id>/', views.edit_album, name='edit album'),
        path('delete/<int:id>/', views.delete_album, name='delete album'),
    ])),
    path('song/', include([
        path('create/', views.create_song, name='create song'),

    ])),
]
