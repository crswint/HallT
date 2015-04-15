from django.contrib.gis.db import models

# Create your models here.


class Stop(models.Model):
    """This model will hold public transit bus stop information"""
    geom = models.PointField(srid=4326)
    name = models.CharField(max_length=40)
    amenities = models.CharField(max_length=40)


class Route(models.Model):
    """This model will hold public transit bus routes information"""
    geom = models.LineStringField(srid=4326)
    route_num = models.CharField(max_length=40)
    stops = models.ManyToManyField(Stop)
