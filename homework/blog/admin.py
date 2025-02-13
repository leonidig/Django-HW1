from django.contrib import admin
from .models import Product, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  
    search_fields = ('name',) 


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'seller')  
    list_filter = ('tags',)  
    search_fields = ('name', 'description')  
    filter_horizontal = ('tags',) 
