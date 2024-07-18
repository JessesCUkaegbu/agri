# cart.py

from decimal import Decimal
from django.conf import settings
from agriApp.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart_data_obj')
        if not cart:
            cart = self.session['cart_data_obj'] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'title': product.title,
                'qty': 0,
                'product_price': str(product.price),
                'product_image': product.image.url,
            }
        if update_quantity:
            self.cart[product_id]['qty'] = quantity
        else:
            self.cart[product_id]['qty'] += quantity
        self.save()

    def save(self):
        self.session['cart_data_obj'] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session['cart_data_obj']
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['product_price']) * item['qty'] for item in self.cart.values())

    def get_subtotal(self):
        return sum(Decimal(item['product_price']) * item['qty'] for item in self.cart.values())

    def get_items(self):
        return [{
            'product': Product.objects.get(id=product_id),
            'title': item['title'],
            'qty': item['qty'],
            'product_price': Decimal(item['product_price']),
            'product_image': item['product_image'],
            'total_price': Decimal(item['product_price']) * item['qty']
        } for product_id, item in self.cart.items()]