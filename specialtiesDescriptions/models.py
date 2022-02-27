from django.db import models
from django.db.models.deletion import CASCADE

class Front(models.Model):
    FrontDecription = models.CharField(max_length=512,blank=False)
    def __str__(self):
        return self.FrontDecription

class BackDecription(models.Model):
    BackDecription = models.CharField(max_length=512,blank=False)
    def __str__(self):
        return self.BackDecription


class FullStackDecription(models.Model):
    FullStackDecription = models.CharField(max_length=512,blank=False)
    def __str__(self):
        return self.FullStackDecription

class UiUxDecription(models.Model):
    UiUxDecription = models.CharField(max_length=512,blank=False)
    def __str__(self):
        return self.UiUxDecription