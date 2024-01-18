from django.db import models
from cloudinary.models import CloudinaryField


class Contributor(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    role = models.CharField(max_length=200)
    headshot = CloudinaryField('image', default='placeholder')
    background = models.TextField()
    motivation = models.TextField()
    fav_place = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        get_latest_by = "created_on"

    def __str__(self):
        return self.name
    
    def joined_us(self):
        return self.created_on.strftime('%b') + ' ' + self.created_on.strftime('%Y')
