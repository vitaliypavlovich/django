
import logging
from django.http import HttpResponse

from django.db.models import Max, Sum, Count
from products.models import Product, Purchase
logger = logging.getLogger(__name__)



def index(request):
    products = Product.objects.all()
    title = request.GET.get('title')
    if title is not None:
        products = products.filter(title__icontains=title)
    purchases__count = request.GET.get('purchases__count')
    if purchases__count is not None:
        products = products.filter(purchases__count=purchases__count)

    # queryset = Product.objects.annotate(purchase__count=Count('purchases'))
    # queryset = queryset.filter(purchase_count_gt=0)
    # print(queryset.first().purchase_count)


    return HttpResponse('<br>'.join([str(p) for p in products]))

