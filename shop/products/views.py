
import logging
from django.http import HttpResponse

from products.models import Product
logger = logging.getLogger(__name__)


def index(request):
    products = Product.objects.all()
    query = request.GET.get('query')
    if query is not None:
        products = products.filter(title__icontains=query)
    return HttpResponse('<br>'.join([str(p) for p in products]))

