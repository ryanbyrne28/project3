from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path('playlists/<int:playlists_id>/', views.playlists_detail, name='detail'), # show
    path('accounts/signup/', views.signup, name='signup'),
]