import os
from django.contrib.gis.utils import LayerMapping
from apps.tran_maps.models import Stop
import django
django.setup()

# Generic load file used in the GeoDjango tutorial.  Left in case more GeoDjango data needs loading
stop_mapping = {
    'name' : 'name',
    'geom' : 'POINT',
    'amenities' : 'amenities',
}

stop_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/stops.shp'))


def run(verbose=True):
    lm = LayerMapping(Stop, stop_shp, stop_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)