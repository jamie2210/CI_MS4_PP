from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404
    )
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

    return render(request, 'favourites/favourites.html')
