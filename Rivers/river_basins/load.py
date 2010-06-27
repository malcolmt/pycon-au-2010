#!/usr/bin/env python
"""
Import river basin data into models.
"""

import os
import sys

from django.contrib.gis import utils

from river_basins import models


VERBOSE = True

FILES = (
    "rbasin_polygon.shp",
    "rbasin_chain.shp",
    "rbasin_point.shp",
)

def main(argv=None):
    if argv is None:
        argv = sys.argv

    directory = sys.argv[1]
    layermapping = utils.LayerMapping(models.RBasinPolygon,
            os.path.join(directory, FILES[0]),
            models.rbasinpolygon_mapping,
            transform=False, encoding="iso-8859-1")
    layermapping.save(strict=True, verbose=VERBOSE)

    layermapping = utils.LayerMapping(models.RBasinChain,
            os.path.join(directory, FILES[1]),
            models.rbasinchain_mapping,
            transform=False, encoding="iso-8859-1")
    layermapping.save(strict=True, verbose=VERBOSE)

    layermapping = utils.LayerMapping(models.RBasinPoint,
            os.path.join(directory, FILES[2]),
            models.rbasinpoint_mapping,
            transform=False, encoding="iso-8859-1")
    layermapping.save(strict=True, verbose=VERBOSE)

if __name__ == "__main__":
    sys.exit(main())

