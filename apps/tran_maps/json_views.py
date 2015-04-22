from apps.tran_maps import models, serializers
from rest_framework import generics
import django_filters


class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split('.')]
            return qs.filter(**{'{}__{}'.format(self.name, self.lookup_type): integers})
        return qs


class RouteFilter(django_filters.FilterSet):
    """ Filter used for the Route model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Route
        fields = ('id', 'route_num')


class StopFilter(django_filters.FilterSet):
    """ Filter used for the Stop model."""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Stop
        fields = ('id', 'name')


class RouteCollection(generics.ListAPIView):
    """
    API endpoint that allows transportation routes to be viewed or edited.
    """
    queryset = models.Route.objects.all()
    serializer_class = serializers.RouteSerializer
    filter_class = RouteFilter


class StopCollection(generics.ListAPIView):
    """
    API endpoint that allows transportation stops to be viewed or edited.
    """
    queryset = models.Stop.objects.all()
    serializer_class = serializers.StopSerializer
    filter_class = StopFilter


class RouteStopsCollection(generics.ListAPIView):
    """
    API endpoint that allows transportation stops to be viewed or edited.
    """
    queryset = models.Stop.objects.all()
    serializer_class = serializers.StopSerializer
    filter_class = StopFilter

    def get_queryset(self):
        route = models.Route.objects.filter(route_num=self.kwargs['route']).first()
        return route.stops.all()