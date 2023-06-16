from django.contrib import admin
from .models import Product, ProductsImage


class ProductImageInline(admin.TabularInline):
    model = ProductsImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
