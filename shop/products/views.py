import logging
from django.core.cache import cache
from django.shortcuts import render, redirect
from products.models import Product
from products.forms import AddProductForm

logger = logging.getLogger(__name__)


def index(request):
    # title = request.GET.get('title')
    # purchases__count = request.GET.get('purchases__count')
    # result = cache.get(f"products-view-{title}-{purchases__count}")
    # if result is not None:
    #     return result

    products = Product.objects.all()
    title = request.GET.get("title")
    if title is not None:
        products = products.filter(title__icontains=title)
    purchases__count = request.GET.get("purchases__count")
    if purchases__count is not None:
        products = products.filter(purchases__count=purchases__count)

    response = render(request, "index.html", {"products": products})
    cache.set(f"products-view-{title}-{purchases__count}", response, 60 * 60)
    return response


def add_product(request):
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(
                title=form.cleaned_data["title"],
                price=form.cleaned_data["price"],
                description=form.cleaned_data["description"],
            )
            logger.info(f"Product name: {form.cleaned_data['title']}")
            logger.info(f"Product price: {form.cleaned_data['price']}")
            return redirect("/")
    else:
        form = AddProductForm()

    return render(request, "add_product.html", {"form": form})
