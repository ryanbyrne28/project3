from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path('playlists/<int:playlist_id>/', views.playlist_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('playlists/', views.playlist_index, name='index'),
    path('playlists/create/', views.PlaylistCreate.as_view(), name='playlist_create'),
    path('playlists/<int:pk>/update/', views.PlaylistUpdate.as_view(), name='playlist_update'),
    path('playlists/<int:pk>/delete/', views.PlaylistDelete.as_view(), name='playlist_delete'),

    path('playlists/<int:playlist_id>/assoc_song/<int:song_id>/', views.assoc_song, name='assoc_song'),
    path('playlists/<int:playlist_id>/remove_song/<int:song_id>/', views.remove_song, name='remove_song'),
    
    path('songs/create/', views.SongCreate.as_view(), name='songs_create'),
    path('songs/', views.SongsIndex.as_view(), name='songs_index'),
    path('songs/<int:pk>/', views.SongsDetail.as_view(), name='songs_detail'),
    path('songs/<int:pk>/update/', views.SongUpdate.as_view(), name='songs_update'),
    path('songs/<int:pk>/delete/', views.SongDelete.as_view(), name='songs_delete'),
]