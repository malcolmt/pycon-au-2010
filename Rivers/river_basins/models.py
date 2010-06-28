"""
Models for importing the river basin data. All the basic model fields and
mapping dictionaries were generated using the "ogrinspect" management command.

I ran something along the lines of:

     ./manage.py ogrinspect --decimal true --mapping rbasin_chain.shp \
         RBasinChain >> river_basins/models.py 

(repeat two more times for rbasin_point.shp and rbasin_polygon.shp).

"""

from django.contrib.gis.db import models

# FIXME: All the PolygonFields should use the AGD66 projection, but that isn't
# known to proj by default, so we ignore the projection for now. It's not too
# far off to just use the default and works for tutorial purposes.

class RBasinPolygon(models.Model):
    area = models.DecimalField(max_digits=31, decimal_places=15)
    perimeter = models.DecimalField(max_digits=31, decimal_places=15)
    aus_field = models.DecimalField(max_digits=11, decimal_places=0)
    aus_id = models.DecimalField(max_digits=11, decimal_places=0)
    f_code = models.CharField(max_length=12)
    bname = models.CharField(max_length=30)
    bnum = models.CharField(max_length=5)
    rname = models.CharField(max_length=35)
    rnum = models.CharField(max_length=5)
    dname = models.CharField(max_length=25)
    dnum = models.CharField(max_length=5)
    centroid_y = models.DecimalField(max_digits=31, decimal_places=15)
    centroid_x = models.DecimalField(max_digits=31, decimal_places=15)
    geom = models.PolygonField()

    objects = models.GeoManager()

    def __unicode__(self):
        return self.bname


class RBasinPoint(models.Model):
    area = models.DecimalField(max_digits=31, decimal_places=15)
    perimeter = models.DecimalField(max_digits=31, decimal_places=15)
    aus_field = models.DecimalField(max_digits=11, decimal_places=0)
    aus_id = models.DecimalField(max_digits=11, decimal_places=0)
    f_code = models.CharField(max_length=12)
    bname = models.CharField(max_length=30)
    bnum = models.CharField(max_length=5)
    rname = models.CharField(max_length=35)
    rnum = models.CharField(max_length=5)
    dname = models.CharField(max_length=25)
    dnum = models.CharField(max_length=5)
    geom = models.PointField()

    objects = models.GeoManager()

    def __unicode__(self):
        return self.bname


class RBasinChain(models.Model):
    fnode_field = models.DecimalField(max_digits=11, decimal_places=0)
    tnode_field = models.DecimalField(max_digits=11, decimal_places=0)
    lpoly_field = models.DecimalField(max_digits=11, decimal_places=0)
    rpoly_field = models.DecimalField(max_digits=11, decimal_places=0)
    length = models.DecimalField(max_digits=31, decimal_places=15)
    aus_field = models.DecimalField(max_digits=11, decimal_places=0)
    aus_id = models.DecimalField(max_digits=11, decimal_places=0)
    f_code = models.CharField(max_length=12)
    geom = models.LineStringField()

    objects = models.GeoManager()

    def __unicode__(self):
        return self.f_code


rbasinchain_mapping = {
    'fnode_field' : 'FNODE_',
    'tnode_field' : 'TNODE_',
    'lpoly_field' : 'LPOLY_',
    'rpoly_field' : 'RPOLY_',
    'length' : 'LENGTH',
    'aus_field' : 'AUS_',
    'aus_id' : 'AUS_ID',
    'f_code' : 'F_CODE',
    'geom' : 'LINESTRING',
}

rbasinpolygon_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'aus_field' : 'AUS_',
    'aus_id' : 'AUS_ID',
    'f_code' : 'F_CODE',
    'bname' : 'BNAME',
    'bnum' : 'BNUM',
    'rname' : 'RNAME',
    'rnum' : 'RNUM',
    'dname' : 'DNAME',
    'dnum' : 'DNUM',
    'centroid_y' : 'CENTROID_Y',
    'centroid_x' : 'CENTROID_X',
    'geom' : 'POLYGON',
}

rbasinpoint_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'aus_field' : 'AUS_',
    'aus_id' : 'AUS_ID',
    'f_code' : 'F_CODE',
    'bname' : 'BNAME',
    'bnum' : 'BNUM',
    'rname' : 'RNAME',
    'rnum' : 'RNUM',
    'dname' : 'DNAME',
    'dnum' : 'DNUM',
    'geom' : 'POINT',
}

