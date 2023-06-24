from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404
    )

from django.http import Http404
from django.contrib import messages
from products.models import Product
from django.contrib.auth.decorators import login_required
from .models import Favourites


@login_required
def view_favourites(request):
    """ A view to return the favourites page """

    favourites_items_count = 0
    favourites_items = None

    favourites = Favourites.objects.filter(username=request.user).first()

    if favourites:
        favourites_items = favourites.products.all()
        favourites_items_count = favourites.products.all().count()

    if not favourites_items:
        messages.info(request, 'Your favourites list is empty!')

    template = 'favourites/favourites.html'
    context = {
        'favourites_items': favourites_items,
        'favourites_items_count': favourites_items_count,
    }

    return render(request, 'favourites/favourites.html', context)


@login_required
def add_to_favourites(request, item_id):
    """
    Add a product item to favourites
    """
    product = get_object_or_404(Product, pk=item_id)

    try:
        favourites = get_object_or_404(Favourites, username=request.user.id)
    except Http404:
        favourites = Favourites.objects.create(username=request.user)

    if product in favourites.products.all():
        messages.info(request, f'{ product.name } is '
                               'already in your favourites!')
    else:
        favourites.products.add(product)
        messages.info(request, f'Added { product.name } to your favourites')

    return redirect(reverse('product_detail', args=[item_id]))


@login_required
def remove_from_favourites_in_favourites(request, item_id):
    """
    Remove a product item from favourites page
    """
    product = get_object_or_404(Product, pk=item_id)
    favourites = get_object_or_404(Favourites, username=request.user.id)

    if product in favourites.products.all():
        favourites.products.remove(product)
        messages.info(request, f'Removed { product.name } '
                               'from your favourites list')
    else:
        messages.error(request, f'{ product.name } is '
                                'not in your favourites list!')

    return redirect(reverse('view_favourites'))


@login_required
def remove_from_favourites_in_products_detail(request, item_id):
    """
    Remove a product item from
    favourites on products detail page
    """
    product = get_object_or_404(Product, pk=item_id)
    favourites = get_object_or_404(Favourites, username=request.user.id)

    if product in favourites.products.all():
        favourites.products.remove(product)
        messages.info(request, f'Removed { product.name } '
                               'from your favourites list')
    else:
        messages.error(request, f'{ product.name } is '
                                'not in your favourites list!')

    return redirect(reverse('product_detail', args=[item_id]))
