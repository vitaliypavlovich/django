from rest_framework import serializers

from products.models import Product



class ProductModelSerializer(serializers.HyperlinkedModelSerializer):

    has_image = serializers.SerializerMethodField()
    purchase_count = serializers.IntegerField()
    purchases_total = serializers.IntegerField()


    def get_has_image(self, obj) -> bool:
        return bool(obj.image)




    class Meta:
        model = Product
        fields = ["id", "title", 'has_image', 'purchase_count', 'purchases_total',
                  "image", "color", "price", "description", "created_at"]