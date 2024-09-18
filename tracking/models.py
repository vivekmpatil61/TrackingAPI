from django.db import models

# Create your models here.

class Parcel(models.Model):
    tracking_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)