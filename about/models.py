from django.db import models
from cloudinary.models import CloudinaryField


class Contributor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    role = models.CharField(max_length=200)
    headshot = CloudinaryField('image', default='placeholder')
    background = models.TextField()
    motivation = models.TextField()
    fav_place = models.CharField(max_length=200)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
