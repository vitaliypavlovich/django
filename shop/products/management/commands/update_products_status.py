import logging

from django.core.management.base import BaseCommand
from django_rq import job

from products.models import Product

logger = logging.getLogger(__name__)


@job
def update_status():
    products = Product.objects.all()
    for product in products:
        if product.price == 0:
            product.status = 'OUT_OF_STOCK'
            product.save()


class Command(BaseCommand):
    help = "Update products status"

    def handle(self, *args, **options):
        update_status.delay()
