from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
    


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    land_length = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    land_width = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_length = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_width = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    product_depth = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    refrigerated = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['created']),
        ]
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name