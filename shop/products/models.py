import os
from decimal import Decimal

from django.conf import settings
from django.db import models


COLOR_CHOICES = (
    ("RED", "Red"),
    ("GREEN", "Green"),
    ("BlUE", "Blue"),
)

STATUS_CHOICES = (
    ("IN_STOCK", "In_stock"),
    ("OUT_OF_STOCK", "Out_of_stock"),
)


class Product(models.Model):
    external_id = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    color = models.CharField(max_length=32, choices=COLOR_CHOICES, default="RED")
    price = models.DecimalField(default=Decimal("0"), decimal_places=5, max_digits=10)
    price_usd = models.DecimalField(
        default=Decimal("0"), decimal_places=5, max_digits=10
    )
    category = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default="IN_STOCK")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Product: {self.title} - {self.price}"

    def delete(self, using=None, keep_parents=False):
        os.remove(self.image.path)
        super().delete(using, keep_parents)


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="purchases"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="purchases"
    )
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Purchase: {self.user} - {self.product} - {self.count}"
