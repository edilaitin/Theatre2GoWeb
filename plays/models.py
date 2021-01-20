from cloudinary.models import CloudinaryField
from django.db import models
from django.db.models.signals import post_save
from star_ratings.models import UserRating

from artists.models import Artist
from theatres.models import Theatre


def on_rating_save(sender, instance, **kwargs):
    print("AAAAAAAAAAAAAAAAAA")


post_save.connect(on_rating_save, sender=UserRating)


class VaultPlay(models.Model):
    title = models.CharField(max_length=255, null=False)
    shortBio = models.TextField()
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    director = models.ForeignKey(Artist, on_delete=models.SET_NULL, related_name="director", null=True)
    writer = models.CharField(max_length=255, null=False)
    image = CloudinaryField('playImage')
    carouselImage1 = CloudinaryField('carouselImage1', blank=True, null=True)
    carouselImage2 = CloudinaryField('carouselImage2', blank=True, null=True)
    carouselImage3 = CloudinaryField('carouselImage3', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Play(models.Model):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    vaultPlay = models.ForeignKey(VaultPlay, on_delete=models.CASCADE)

    def __str__(self):
        return self.vaultPlay.title
