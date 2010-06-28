The Powerhouse Museum (http://www.powerhousemuseum.com/ ) in Sydney is an
interesting collection of Australian contemporary and historical memorabilia.
Well worth a visit if you've got half a day to kill in Sydney some time.

The dataset used in this talk is a textual summary of all the items in the
museum's collection and can be downloaded from
http://www.powerhousemuseum.com/collection/database/download.php . The data is
licensed under a Creative Commons Attribution-Sharealike 2.5 Australia license.
This particular tutorial used a version that was downloaded on June 22, 2010,
but there's nothing particularly special about that copy.

As explained in the talk, the importing code (load.py) expects two files. The
first is a list of categories, one per line with repitions permitted. The
second is the unadulterated Powerhouse dataset. The categories file can be
generated (on a Unix-like system) via:

    tail -n +2 phm_collection.txt | cut -f9 | grep -v "^$" | tr "|" "\n" \
            > categories.txt

You can also generate the same file (with a few extra blanks, which are
harmless) using the Python one-liner (split over two lines for readability, but
it should be a single line):

    python -c "print '\n'.join(l.split('\t')[8].replace('|', '\n')
            for l in open('phm_collection.txt').readlines())" > categories.txt

and then removing the first line ("Categories"), which is the header line and
not a real category name.

When "python manage.py syncdb --noinput" is run to initialise the database, an
admin user with username "admin" and password "admin" will automatically be
created. The currents settings use a local sqlite database. However, for speed
of import when I was developing this, I used an sqlite database on a
memory-backed filesystem (in Linux). I ran:

    mount -t tmpfs -o uid=500,gid=500 tmpfs /home/malcolm/store
    # Changed settings.py to put the database in ~/store/phm.sqlite
    PYTHONPATH=.. DJANGO_SETTINGS_MODULE=settings ./load.py \
            categories.txt phm_collection.txt

Using this setup (memory-backed filesystem), it takes just over 5 minutes to
import the full dataset using a single 2.5GHz core on my laptop.

