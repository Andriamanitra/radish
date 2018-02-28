from django.db import models

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length = 127, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class StationUrl(models.Model):
    url = models.URLField(max_length = 127, unique=True)
    station = models.ForeignKey(Station, related_name="urls", on_delete=models.CASCADE)
    
    def extension(self):
        if len(self.url[-5:].rsplit(".", 1)) == 2:
            return "."+self.url[-5:].rsplit(".", 1)[1]
        else:
            return "stream"
    
    def __str__(self):
        return self.url
