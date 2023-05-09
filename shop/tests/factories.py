import factory

from factory.django import DjangoModelFactory

from products.models import Product, Purchase

from decimal import Decimal

from profiles.models import Profile

from random import randint

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker('word')
    color = 'RED'
    price = Decimal(290)
    price_usd = Decimal(100)



class UserFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    first_name = factory.Faker.name()
    age = randint(1, 50)


class PurchaseFactory(DjangoModelFactory):
    class Meta:
        model = Purchase

    user = 'aloaaa'
    product = 'Дрель-шуруповерт Werker EWCDL 814'
    count = randint(1, 100)