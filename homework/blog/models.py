from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.




class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    added_at = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")

    def get_absolute_url(self):
        return reverse('blog:product_detail', args=[self.id])
    

class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
    quantity = models.PositiveIntegerField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return f"Order({self.buyer}; {self.product}; {self.quantity}, {self.ordered_at})"
