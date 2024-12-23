from django.db import models
from products.models import Product

class Advertisement(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='advertisements')
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name