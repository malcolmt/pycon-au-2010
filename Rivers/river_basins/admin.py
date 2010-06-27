from django.contrib.gis import admin

from river_basins import models

admin.site.register([models.RBasinPolygon, models.RBasinChain,
        models.RBasinPoint], admin.GeoModelAdmin)

