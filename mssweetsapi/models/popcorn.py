from django.db import models


class Popcorn(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.URLField(max_length=300)
