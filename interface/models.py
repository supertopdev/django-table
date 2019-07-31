from django.db import models

# Create your models here.
from django.db.models import Model


class Centris(models.Model):
    pid = models.CharField(max_length=255, null=False, blank=False)
    centris_title = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    workscore = models.CharField(max_length=255, null=True, blank=True)
    beds_baths = models.CharField(max_length=255, null=True, blank=True)
    geo_cordinates = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=5000, null=True, blank=True)
    agent_name = models.CharField(max_length=255, null=True, blank=True)
    built_year = models.CharField(max_length=255, null=True, blank=True)
    construction_year = models.CharField(max_length=255, null=True, blank=True)
    available_area = models.CharField(max_length=255, null=True, blank=True)
    lot_area = models.CharField(max_length=255, null=True, blank=True)
    operation_type = models.CharField(max_length=255, null=True, blank=True)
    fireplace_stove = models.CharField(max_length=255, null=True, blank=True)
    additional_features = models.CharField(max_length=255, null=True, blank=True)
    potential_gross_revenue = models.CharField(max_length=255, null=True, blank=True)
    main_unit = models.CharField(max_length=255, null=True, blank=True)
    residential_units = models.CharField(max_length=255, null=True, blank=True)
    unit_number = models.CharField(max_length=255, null=True, blank=True)
    parking = models.CharField(max_length=255, null=True, blank=True)
    building_area = models.CharField(max_length=255, null=True, blank=True)
    use_property = models.CharField(max_length=255, null=True, blank=True)
    zoning = models.CharField(max_length=255, null=True, blank=True)
    residential_unit = models.CharField(max_length=255, null=True, blank=True)
    business_type = models.TextField(max_length=1000, null=True, blank=True)
    intergenerational = models.CharField(max_length=255, null=True, blank=True)
    building_style = models.CharField(max_length=255, null=True, blank=True)
    pool = models.CharField(max_length=255, null=True, blank=True)
    condominium = models.CharField(max_length=255, null=True, blank=True)
    gross_area = models.CharField(max_length=255, null=True, blank=True)
    net_area = models.CharField(max_length=255, null=True, blank=True)
    property_current_active = models.IntegerField(max_length=10, null=False, blank=False)

    class Meta:
        db_table = 'centris_table'
