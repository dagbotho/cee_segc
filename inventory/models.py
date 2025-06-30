from django.db import models

# Create your models here.
class ConstructionSite(models.Model):
    site_name = models.CharField(max_length=255)
    site_address = models.CharField(max_length=255)
    site_phone_number = models.CharField(max_length=20)
    site_email = models.EmailField(max_length=255, blank=True, null=True)
    site_country = models.CharField(max_length=255)
    site_city = models.CharField(max_length=255)
    site_postal_code = models.CharField(max_length=20)