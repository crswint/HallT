import json
import shapefile
from . import models
import django
django.setup()

#Custom load file created to load Center model into database
route_path = 'C:/Users/crswin5726/PycharmProjects/HAllT/apps/tran_maps/data/routes.shp'

sf = shapefile.Reader(route_path)
sr = sf.shapeRecords()
record = {-1: True, 0: False}

for r in sr:
    route_num = r.record[0]
    if not models.Route.objects.filter(route_num=route_num).exists():
        route = models.Route(route_num=route_num,
                             geom=json.dumps(r.shape.__geo_interface__))

        route.save()
    stops = [s.strip() for s in r.record[1].split(',')]
    stops = models.Stop.objects.filter(pk__in=stops)
    if len(stops) > 0:
        route = models.Route.objects.filter(route_num=route_num).first()
        if len(route.stops.all()) == 0:
            for stop in stops:
                route.stops.add(stop)
            route.save()




