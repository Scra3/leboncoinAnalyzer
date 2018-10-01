from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField
    price = models.FloatField(max_length=30)
    city_label = models.CharField(max_length=5)
