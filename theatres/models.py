from django.db import models
from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField


class TheatreType(models.Model):
    type = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.type


class Theatre(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    phone = PhoneNumberField(null=False, blank=False)
    mail = models.EmailField()
    website = models.CharField(max_length=255, null=True)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    address = models.CharField(max_length=255, null=False, default='Timisoara, Romania')
    image = CloudinaryField('theatreImage')
    theatreType = models.ForeignKey(TheatreType, on_delete=models.CASCADE)  # DELETE ALL THEATRES OF THE DELETED TYPE

    def __str__(self):
        return self.name


class WorkProgram(models.Model):
    theatre = models.OneToOneField(Theatre, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, null=False)
    Monday = models.CharField(max_length=255, null=False)
    Tuesday = models.CharField(max_length=255, null=False)
    Wednesday = models.CharField(max_length=255, null=False)
    Thursday = models.CharField(max_length=255, null=False)
    Friday = models.CharField(max_length=255, null=False)
    Saturday = models.CharField(max_length=255, null=False)
    Sunday = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.description



