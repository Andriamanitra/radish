from django.db import models


class Station(models.Model):
    name = models.CharField(max_length=127, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class StationUrl(models.Model):
    url = models.URLField(max_length=127, unique=True)
    station = models.ForeignKey(Station, related_name="urls",
                                on_delete=models.CASCADE)

    def extension(self):
        return self.url.rsplit(".", 1)[-1]

    def __str__(self):
        return self.url
