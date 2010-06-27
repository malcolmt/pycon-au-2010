#!/usr/bin/env python
"""
Loads the Powerhouse Museum data dump (a tab-separated file) into the data
models.
"""

import csv
import decimal
import re
import sys

from django.conf import settings

from phm_collection import models


# Input file encoding
ENCODING = "iso-8859-1"

weight_pattern = re.compile(r"(\d+(?:\.\d+)?) (kg|g(?:m?))$")
dimension_pattern = re.compile(r"(\d*(?:\.\d+)?) (m|mm|cm)(?:\.|\\)?$")

def main(argv=None):
    assert settings.DEBUG == False, \
            "It's a really bad idea to run this importer with DEBUG = True!"
    if argv is None:
        argv = sys.argv
    category_map = import_categories(argv[1])
    import_records(argv[2], category_map)

def import_categories(filename):
    """
    Creates Category records for each category name in filename (a file with
    one name per line). Each name is normalised to the title case version of
    the name, to remove some duplicates.

    Can safely be run more than once on the same file, as any existing names
    are skipped in the import phase.

    Returns a dictionary mapping names to object_ids, which avoids extra
    database lookups when items are imported.
    """
    category_map = dict(models.Category.objects.values_list("name", "id"))
    names = set(line.strip().title() for line in open(filename).readlines()
            if line)
    names.difference_update(category_map.keys())
    current = 0
    for name in names:
        obj = models.Category.objects.create(name=name)
        category_map[name] = obj.id
        current += 1
        if current % 100 == 0:
            print "Imported %d categories." % current
    return category_map

def import_records(filename, category_map):
    """
    Import item records, skipping over any that have already been imported.
    """
    existing = set(models.Item.objects.values_list("record_id", "title"))
    fieldnames = (
        "record_id",
        "title",
        "reg_number",
        "description",
        "marks",
        "prod_date",
        "provenance_prod",
        "provenance_historical",
        "categories",
        "permalink",
        "height",
        "width",
        "depth",
        "diameter",
        "weight",
        "license_info",
    )
    convert_fields = (
        "record_id",
        "title",
        "reg_number",
        "description",
        "marks",
        "provenance_prod",
        "provenance_historical",
        "license_info",
    )
    reader = csv.DictReader(open(filename), fieldnames, delimiter="\t",
            quoting=csv.QUOTE_NONE)
    reader.next()
    current = 0
    for entry in reader:
        if (entry["record_id"], entry["title"].decode(ENCODING)) in existing:
            # Avoids multiple imports of the same data.
            continue

        # DEBUG:
        # import pprint
        # pprint.pprint(entry)
        # print

        for name in ("height", "width", "depth", "diameter"):
            entry[name] = normalise_dimension(entry[name], current)
        entry["weight"] = normalise_weight(entry["weight"], current)
        for key in convert_fields:
            entry[key] = entry[key].decode(ENCODING)
        categories = entry.pop("categories")
        item = models.Item.objects.create(**entry)

        category_names = [c.strip().title() for c in categories.split("|") if c]
        category_ids = [category_map[name] for name in category_names]
        item.categories = category_ids

        current += 1
        if current % 500 == 0:
            print "Handled %d." % current

def normalise_dimension(value, count):
    value = value.strip().lower()
    if not value:
        return None
    match = dimension_pattern.match(value)
    assert match is not None, "Bad dimension in entry %d: %s" % (count, value)
    dimension = decimal.Decimal(match.group(1))
    if match.group(2) == "m":
        dimension *= 1000
    if match.group(2) == "cm":
        dimension *= 10
    return dimension

def normalise_weight(value, count):
    value = value.strip().lower()
    if not value:
        return None
    match = weight_pattern.match(value)
    assert match is not None, "Bad weight entry line %d: %s" % (count, value)
    weight = decimal.Decimal(match.group(1))
    if match.group(2) == "gm":
        weight /= 1000
    return weight

if __name__ == "__main__":
    sys.exit(main())

