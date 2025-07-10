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


class Transfer(models.Model):
    transfer_date = models.DateField(auto_now_add=True)
    transfer_quantity = models.PositiveIntegerField()
    transfer_from = models.ForeignKey(ConstructionSite, related_name='transfers_from', on_delete=models.CASCADE)
    transfer_to = models.ForeignKey(ConstructionSite, related_name='transfers_to', on_delete=models.CASCADE)
    transfer_description = models.TextField(blank=True, null=True)
    transfer_received_date = models.DateField(blank=True, null=True)
    product_id = models.ForeignKey('shop.Product', related_name='product', on_delete=models.CASCADE, blank=True, null=True)
    warehouse_id = models.ForeignKey('Warehouse', related_name='warehouse', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Transfer from {self.transfer_from.site_name} to {self.transfer_to.site_name} on {self.transfer_date}"
    

class Stock(models.Model):
    product_name = models.CharField(max_length=255)
    quantity_available = models.PositiveIntegerField()
    minimum_stock_level = models.PositiveIntegerField()
    maximum_stock_level = models.PositiveIntegerField()
    reorder_point = models.PositiveIntegerField()
    product_id = models.ForeignKey('shop.Product', related_name='product', on_delete=models.CASCADE, blank=True, null=True)
    warehouse_id = models.ForeignKey('Warehouse', related_name='warehouse', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.product_name
    

class WarehouseCategory(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name
    
class Warehouse(models.Model):
    warehouse_name = models.CharField(max_length=255)
    warehouse_address = models.CharField(max_length=255)
    warehouse_phone_number = models.CharField(max_length=20)
    warehouse_email = models.EmailField(max_length=255, blank=True, null=True)
    warehouse_country = models.CharField(max_length=255)
    warehouse_city = models.CharField(max_length=255)
    warehouse_postal_code = models.CharField(max_length=20)
    category_warehouse_id = models.ForeignKey(WarehouseCategory, on_delete=models.CASCADE, blank=True, null=True)
    isRefrigerated = models.BooleanField(default=False)
    location_id = models.ForeignKey('Location', on_delete=models.CASCADE, blank=True, null=True)
    order_detail_id = models.ForeignKey('orders.OrderItem', related_name='Orderitem', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.warehouse_name
    

class Delivery(models.Model):
    sales_date = models.DateField(auto_now_add=True)
    customer_id = models.ForeignKey('Marketing.Customer', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Delivery from {self.delivery_from.warehouse_name} to {self.delivery_to.site_name} on {self.delivery_date}"
    

class DeliveryDetail(models.Model):
    quantity_delivered = models.PositiveIntegerField()
    expecteed_date_of_delivery = models.DateField(blank=True, null=True)
    actual_date_of_delivery = models.DateField(blank=True, null=True)
    delivery_id = models.ForeignKey(Delivery, related_name='delivery', on_delete=models.CASCADE)
    product_id = models.ForeignKey('shop.Product', related_name='product', on_delete=models.CASCADE)
    warehouse_id = models.ForeignKey(Warehouse, related_name='warehouse', on_delete=models.CASCADE, blank=True, null=True)

    
    class Meta:
        unique_together = ('quantity_delivered')


class Location(models.Model):
    location_name = models.CharField(max_length=255)
    location_address = models.CharField(max_length=255)
    location_country = models.CharField(max_length=255)
    location_city = models.CharField(max_length=255)
    location_postal_code = models.CharField(max_length=20)

    def __str__(self):
        return self.location_name