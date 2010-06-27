This project contains code and models for importing data about Australia's river basins. It uses data from 1997, updated slightly over the years up to 2004. I downloaded the version I used on June 22, 2010.

Data is available from https://www.ga.gov.au/products/servlet/controller?event=GEOCAT_DETAILS&catno=42343 and is licensed under the Creative Commons Attribute 3.0 Australia license (http://creativecommons.org/licenses/by/3.0/au/). The *_shp.zip file is a 13 M download and that's the one I was using here (SHP datafiles are easy to use with GeoDjango).

That license applies to the Australian Government Geoscience data (which isn't included in this package for space reasons). My own original code and test are licensed under the terms in the README.txt file in the parent directory.

I used a PostGIS database to load the data:

	createdb -T postgis_template rivers
	./manage.py syncdb --noinput
	cd river_basins
	PYTHONPATH=.. DJANGO_SETTINGS_MODULE=settings /load.py <shapefile_dir>

The code here provides a way to load the data and view it in the admin.

