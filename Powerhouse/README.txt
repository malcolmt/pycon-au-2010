The Powerhouse Museum (http://www.powerhousemuseum.com/ ) in Sydney is an
interesting collection of Australian contemporary and historical memorabilia.
Well worth a visit if you've got half a day to kill in Sydney some time.

The dataset used in this talk is a textual summary of all the items in the
museum's collection and can be downloaded from
http://www.powerhousemuseum.com/collection/database/download.php . The data is
licensed under a Creative Commons Attribution-Sharealike 2.5 Australia license.
This particular tutorial used a version that was downloaded on June 22, 2010,
but there's nothing particularly special about that copy.

When "python manage.py syncdb --noinput" is run to initialise the database, an
admin user with username "admin" and password "admin" will automatically be
created. The currents settings use a local sqlite database. However, for speed
of import when I was developing this, I used an sqlite database on a
memory-backed filesystem (in Linux). I ran:

	mount -t tmpfs -o uid=500,gid=500 tmpfs /home/malcolm/store
	# Changed settings.py to put the database in ~/store/phm.sqlite
	PYTHONPATH=.. DJANGO_SETTINGS_MODULE=settings ./load.py \
			categories.txt phm_collection.txt 

