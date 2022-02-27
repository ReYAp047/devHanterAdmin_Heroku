from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField


class Description(models.Model):
    Description = models.CharField(max_length=512,blank=False)
    def __str__(self):
        return self.Description

