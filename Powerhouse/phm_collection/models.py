from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        # pylint: disable-msg=W0232
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.name


class Item(models.Model):
    # Sadly, record_id is *not* unique in the source data.
    record_id = models.CharField("Record ID", max_length=10)
    title = models.CharField("Object Title", max_length=500)
    reg_number = models.CharField("Registration Number", max_length=25,
            blank=True)
    description = models.TextField(blank=True)
    marks = models.TextField( blank=True)
    # Production date is a bit too freeform to parse sensibly at the moment.
    prod_date = models.CharField("Production Date", max_length=30, blank=True)
    provenance_prod = models.TextField("Provenance (Production)", blank=True)
    provenance_historical = models.TextField("Provenance (History)", blank=True)
    categories = models.ManyToManyField(Category)
    permalink = models.URLField("Persistent Link", verify_exists=False)
    height = models.PositiveIntegerField("Height in mm", blank=True, null=True)
    width = models.PositiveIntegerField("Width in mm", blank=True, null=True)
    depth = models.PositiveIntegerField("Depth in mm", blank=True, null=True)
    diameter = models.PositiveIntegerField("Diameter in mm", blank=True,
            null=True)
    weight = models.DecimalField("Weight in kg", max_digits=13,
            decimal_places=5, blank=True, null=True)
    # This contains raw HTML; pass through "safe" filter in templates.
    license_info = models.TextField()

    def __unicode__(self):
        return self.title

