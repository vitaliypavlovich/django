from rest_framework import serializers

from products.models import Product



class ProductModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "image", "color", "price", "description", "created_at"]