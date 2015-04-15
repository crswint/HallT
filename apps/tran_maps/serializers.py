from apps.tran_maps import models
from rest_framework_gis import serializers as geoserializers


class RouteSerializer(geoserializers.GeoFeatureModelSerializer):
    """ Serializer used in API set up off the Route model."""
    class Meta:
        model = models.Route
        geo_field = 'geom'
        fields = ('id', 'route_num', 'stops')


class StopSerializer(geoserializers.GeoFeatureModelSerializer):
    """ Serializer used in API set up off the Stop model."""
    class Meta:
        model = models.Stop
        geo_field = 'geom'
        fields = ('id', 'name', 'amenities')
