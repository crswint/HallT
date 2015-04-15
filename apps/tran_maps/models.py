from django.contrib.gis.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.

fs = FileSystemStorage(location='/media/photos')


class Stop(models.Model):
    """This model will hold public transit bus stop information"""
    geom = models.PointField(srid=4326)
    name = models.CharField(max_length=40)
    amenities = models.CharField(max_length=40)

    def __str__(self):
        return "{}".format(self.name)


class Route(models.Model):
    """This model will hold public transit bus routes information"""
    geom = models.MultiLineStringField(srid=4326)
    route_num = models.CharField(max_length=40)
    stops = models.ManyToManyField(Stop)

    def __str__(self):
        return "{}".format(self.route_num)

# class Images(models.Model):
#     """Pics model."""
#     name = models.CharField(max_length=100)
#     place = models.ForeignKey(Stop)
#     photo = models.ImageField(storage=fs)
#
#     def __str__(self):
#         return self.name