# Generated by Django 4.2 on 2023-05-01 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_playlists_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlists',
            name='image',
        ),
    ]
