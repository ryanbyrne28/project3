from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

	
class Song(models.Model):
	title=models.CharField()
	artist=models.CharField()
	image=models.ImageField()
	audio_file=models.FileField()
	audio_link=models.CharField(max_length=150,blank=True,null=True)
	duration=models.CharField(max_length=20,blank=True,null=True)
	paginate_by=2

	def __str__(self):
		return f"{self.title}"
	
	def get_absolute_url(self):
		return reverse('songs_detail', kwargs={'pk': self.id})
	
class Playlist(models.Model):
	name=models.CharField(max_length=50)
	description=models.TextField(max_length=250)
	user=models.ForeignKey(User, on_delete=models.CASCADE)

	songs = models.ManyToManyField(Song)

	def __str__(self):
		return f"{self.name}"
	
	def get_absolute_url(self):
		return reverse('detail', kwargs={'playlist_id': self.id})


	