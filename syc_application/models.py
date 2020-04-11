from django.db import models
from django.conf import settings


# Create your models here.

class script(models.Model):
    name = models.CharField(max_length=50, unique=True)
    context = models.CharField(max_length=200, null=False, blank=False)