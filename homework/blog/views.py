from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Product, User


def home_page(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)  
    return render(request, "product_info.html", {"product": product})\
    

def create_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = int(request.POST.get("price"))
        seller = get_object_or_404(User, id=1)
        try :
            product = Product(name=name,
                              description=description,
                              price=price,
                              seller=seller
                            )
            product.full_clean()
        except Exception as e:
            return HttpResponse(f"<h1>Invalid Data: {e}</h1>")

        else:
            product.save()
        return redirect("blog:home")
    return render(request, "create_product.html")