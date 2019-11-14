from django.shortcuts import render
from .models import Product

#
def product_list(request):
    products = Product.objects.all()
    context = { "products": products}
    template = 'Product/product-list.html'
    return render(request, template, context)


def product_detail(request, product_slug):
    product_detail = Product.objects.get(slug=product_slug)
    context = { "product_detail": product_detail}
    template = 'Product/product-detail.html'
    return render(request, template, context)
