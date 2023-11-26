from django.db import models

# Create your models here.

class RealState(models.Model):
    title = models.CharField(max_length=255)
    designation = models.TextField()
    type = models.CharField(max_length=255)
    photo = models.CharField(max_length=255)
    created_at = models.DateField()