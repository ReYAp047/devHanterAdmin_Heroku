from django.db import models
from django.db.models.deletion import CASCADE
from cloudinary.models import CloudinaryField

class Adresse(models.Model):
    Adresse = models.CharField(max_length=512,blank=False)
    def __str__(self):
        return self.Adresse

class Phone(models.Model):
    Phone = models.CharField(max_length=512,blank=False)
    def __str__(self):
        return self.Phone


class Email(models.Model):
    Email = models.CharField(max_length=512,blank=False)
    def __str__(self):
        return self.Email