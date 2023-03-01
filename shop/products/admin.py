from django.contrib import admin

from products.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ("title", "price", "description", "created_at")
   fields = ("title", "price", "description", "created_at")
   readonly_fields = ("created_at",)
   search_fields = ("title", "price")
