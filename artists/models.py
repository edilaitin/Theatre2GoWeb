from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models

from theatres.models import Theatre


class Artist(models.Model):
    name = models.CharField(max_length=255, null=False)
    shortBio = models.TextField()
    image = CloudinaryField('artistImage')
    associatedTheatres = models.ManyToManyField(Theatre)

    def __str__(self):
        return self.name


class ActorRole(models.Model):
    from plays.models import VaultPlay
    vaultPlay = models.ForeignKey(VaultPlay, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, null=False)


class UserFollow(models.Model):
    from plays.models import VaultPlay
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    artists = models.ManyToManyField(Artist)
    plays = models.ManyToManyField(VaultPlay)
    theatres = models.ManyToManyField(Theatre)
