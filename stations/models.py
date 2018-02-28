from django.db import models

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length = 127)
    description = models.TextField()

class StationUrl(models.Model):
    url = models.URLField(max_length = 127)
    station = models.ForeignKey(Station, related_name = "urls")
