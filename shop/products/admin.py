from django.contrib import admin

from products.models import Product
from products.models import Purchase


class PurchaseAdminInline(admin.StackedInline):
    model = Purchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "image",
        "price",
        "price_usd",
        "description",
        "color",
        "status",
        "created_at",
    )
    fields = (
        "title",
        "category",
        "image",
        "price",
        "price_usd",
        "description",
        "color",
        "status",
        "created_at",
    )
    readonly_fields = ("created_at",)
    search_fields = (
        "title",
        "category",
        "price",
        "price_usd",
        "status",
    )
    inlines = (PurchaseAdminInline,)

    def save_form(self, request, form, change):
        return super().save_form(request, form, change)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("user", "product", "count", "created_at")
    fields = ("user", "product", "count", "created_at")
    readonly_fields = ("created_at",)
    search_fields = ("user__email", "product__title")
