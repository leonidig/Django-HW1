from django.urls import path

from .views import product_detail, home_page, create_product

app_name = "blog"

urlpatterns = [
    path('home/', home_page, name='home'),
    path("products/<int:product_id>", product_detail, name="product_detail"),
    path("create_product", create_product, name="create_product")
]