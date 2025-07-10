from django.db import models

# Create your models here.
class Customer(models.Model):
    cust_first_name = models.CharField(max_length=50)
    cust_last_name = models.CharField(max_length=50)
    cust_email = models.EmailField()
    cust_phone_number = models.CharField(max_length=20, blank=True, null=True)
    cust_address = models.CharField(max_length=250, blank=True, null=True)
    cust_city = models.CharField(max_length=100, blank=True, null=True)
    cust_postal_code = models.CharField(max_length=20, blank=True, null=True)
    cust_country = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'