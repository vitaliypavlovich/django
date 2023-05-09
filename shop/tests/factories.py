import factory

from factory.django import DjangoModelFactory

from products.models import Product

from decimal import Decimal

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker('word')
    color = 'RED'
    price = Decimal(290)
    price_usd = Decimal(100)