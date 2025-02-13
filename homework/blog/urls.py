from django.urls import path

from .views import product_detail, home_page, create_product, get_product_by_tag

app_name = "blog"

urlpatterns = [
    path('home/', home_page, name='home'),
    path("products/<int:product_id>", product_detail, name="product_detail"),
    path("create_product/", create_product, name="create_product"),
     path('tags/<int:tag_id>/', get_product_by_tag, name='get_product_by_tag'),
]