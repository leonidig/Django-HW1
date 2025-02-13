from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Product, User, Tag


def home_page(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  
    if request.method == "POST":
        product.delete()
        messages.success(request, f"Product '{product.name}' deleted !")
        return redirect("blog:home")
    return render(request, "product_info.html", {"product": product})\
    

def create_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = float(request.POST.get("price")) 
        seller = get_object_or_404(User, id=1)  
        
        try:
            product = Product(name=name, description=description, price=price, seller=seller)
            product.full_clean()
        except Exception as e:
            return HttpResponse(f"<h1>Invalid Data: {e}</h1>")

        else:
            product.save()
            tags_id = request.POST.getlist("tags")
            tags = Tag.objects.filter(id__in=tags_id) 
            product.tags.set(tags)
            return redirect("blog:home") 

    tags = Tag.objects.all()
    return render(request, "create_product.html", {"tags": tags})


def get_product_by_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    products = Product.objects.filter(tags=tag)
    data = {
        "tag": tag,
        "products": products
    }
    return render(request, "product_by_tag.html", data)