from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponse,
    get_object_or_404
    )
from django.contrib import messages
from products.models import Product
from decimal import Decimal


def view_bag(request):
    """ A view that renders the bag content """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST.get('product_size')
    bag = request.session.get('bag', {})

    if size:
        if product.has_sizes:
            if size == 'a4':
                price_value = Decimal(product.A4_price)
            elif size == 'a3':
                price_value = Decimal(product.A3_price)
            elif size == 'a2':
                price_value = Decimal(product.A2_price)
            elif size == 'a1':
                price_value = Decimal(product.A1_price)
            elif size == 'a0':
                price_value = Decimal(product.A0_price)
        else:
            price_value = Decimal(product.price)

        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name} '
                    f'quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} to your bag')
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added size {size.upper()} {product.name} to your bag')

        total_cost = quantity * Decimal(price_value)
        bag[item_id]['total_cost'] = float(total_cost)

    if not size:
        if quantity > 0:
            if quantity > product.stock:
                messages.error(
                    request, f'Limited stock, only { product.stock } \
                left of { product.name }. Please adjust the quantity.')
            else:
                total_quantity = quantity
                if item_id in bag:
                    total_quantity += bag[item_id].get('quantity', 0)

                if total_quantity > product.stock:
                    messages.error(
                        request, f'Limited stock, only { product.stock } \
                    left of { product.name }. Stock level reached.')
                else:
                    if item_id in list(bag.keys()):
                        if 'quantity' in bag[item_id]:
                            bag[item_id]['quantity'] += quantity
                            messages.success(
                                request, f'Updated {product.name} \
                                quantity in bag')
                        else:
                            bag[item_id]['quantity'] = quantity
                            messages.success(
                                request, f'Added {quantity} x {product.name} \
                            to bag')
                    else:
                        bag[item_id] = {'quantity': quantity}
                        messages.success(
                            request, f'Added {quantity} x {product.name} \
                            to bag')

                total_cost = bag[item_id][
                            'quantity'] * Decimal(product.price)
                bag[item_id]['total_cost'] = float(total_cost)

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified
        product to the specified amount """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name}'
                    f'quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                    request,
                    f'Removed size {size.upper()} {product.name}'
                    'from your bag')
    if not size:
        if quantity > 0:
            if quantity > product.stock:
                messages.error(
                    request, f'Limited stock, only { product.stock } \
                left of { product.name }. Please adjust the quantity.')
            else:
                bag[item_id]['quantity'] = quantity
                messages.success(
                    request, f'Updated quantity of\
                         {product.name} to {quantity}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_item(request, item_id):
    """ Remove the item from the bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name}'
                'from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
