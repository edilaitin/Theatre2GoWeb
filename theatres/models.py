from django.db import models
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField


class TheatreType(models.Model):
    type = models.CharField(max_length=255, null=False)


class WorkProgram(models.Model):
    Monday = models.CharField(max_length=255, null=False)
    Tuesday = models.CharField(max_length=255, null=False)
    Wednesday = models.CharField(max_length=255, null=False)
    Thursday = models.CharField(max_length=255, null=False)
    Friday = models.CharField(max_length=255, null=False)
    Saturday = models.CharField(max_length=255, null=False)
    Sunday = models.CharField(max_length=255, null=False)


class Theatre(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    phone = PhoneNumberField(null=False, blank=False)
    mail = models.EmailField()
    location = PlainLocationField(based_fields=['city'], zoom=7)
    image = CloudinaryField('theatreImage')
    theatreType = models.ForeignKey(TheatreType, on_delete=models.CASCADE)  # DELETE ALL THEATRES OF THE DELETED TYPE
    playsRating = models.IntegerField(editable=False, default=-1)
    program = models.ForeignKey(WorkProgram, on_delete=models.SET_NULL, null=True)
