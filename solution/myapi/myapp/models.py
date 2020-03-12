from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
