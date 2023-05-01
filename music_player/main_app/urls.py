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
]