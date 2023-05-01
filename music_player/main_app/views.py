from django.shortcuts import render, redirect
from .models import Playlist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
    return render(request, "about.html")

def about(request):
    return render(request, "about.html")

@login_required
def playlist_detail(request, playlist_id):
  playlist = Playlist.objects.get(id=playlist_id)
  return render(request, 'playlists/detail.html', { 'playlist': playlist})

@login_required
def playlist_index(request):
    playlist = Playlist.objects.all()
    return render(request, "playlists/index.html", {"playlists": playlist})


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class PlaylistCreate(LoginRequiredMixin, CreateView):
  model = Playlist
  fields = ('name', 'description')

  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the hedgehog
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class PlaylistUpdate(LoginRequiredMixin, UpdateView):
  model = Playlist
  fields = ['name', 'description']

class PlaylistDelete(LoginRequiredMixin, DeleteView):
  model = Playlist
  success_url = '/playlists/'