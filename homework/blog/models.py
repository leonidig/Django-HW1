from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    tags = models.ManyToManyField(Tag, related_name="products")

    def get_absolute_url(self):
        return reverse('blog:product_detail', args=[self.id])
    