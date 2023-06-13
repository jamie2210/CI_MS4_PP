from django.shortcuts import (
    render,
    redirect,
    reverse,
    get_object_or_404
    )
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    """ A view to show all products in random order
        including searching and sorting
    """

    products = Product.objects.all()
    query = None
    categories = None
    random_order = False

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if 'random' in request.GET:
            random_order = True

    if random_order:
        products = products.order_by('?')

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'random_order': random_order,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show details of a specific product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
