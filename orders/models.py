from django.db import models


# Create your models here.
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    third_party = models.ForeignKey('finance.ThirdParty', related_name='orders', on_delete=models.CASCADE, blank=True, null=True)
    

    class Meta:
        ordering = ('-created',)
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return f'Order {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey('shop.Product', related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity