from django.shortcuts import render, get_object_or_404

from .models import Product


def home_page(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  
    return render(request, "product_info.html", {"product": product})