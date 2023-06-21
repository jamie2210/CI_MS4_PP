from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data, in bag.items():
        if isinstance(item_data, dict) and 'items_by_size' in item_data:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                quantity = Decimal(quantity)
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
                total += quantity * price_value
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'price': price_value,
                })
        else:
            if isinstance(item_data, dict):
                quantity = item_data.get('quantity', 0)
                product = get_object_or_404(Product, pk=item_id)
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'price': product.price,
                    'stock': product.stock,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = round(delivery + total, 2)

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
