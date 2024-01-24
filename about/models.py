from django.db import models
from cloudinary.models import CloudinaryField


class Contributor(models.Model):
    """
    Contributor model. Stores a single contributor/team member
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    role = models.CharField(max_length=200)
    headshot = CloudinaryField('image', default='placeholder')
    background = models.TextField()
    motivation = models.TextField()
    fav_place = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Orders contrbiutors alphabetically in admin.
        Gets the latest/most recently added contributor.
        """
        ordering = ['name']
        get_latest_by = "created_on"

    def __str__(self):
        return self.name

    def joined_us(self):
        """
        Creates a cleaner looking date in a month/year format
        e.g. Jan, 2024
        """
        return (
            self.created_on.strftime('%b')
            + ' ' +
            self.created_on.strftime('%Y')
            )
