from .cart import Cart

def cart_total(request):
    cart = Cart(request)
    total_cost = cart.get_total_price()
    return {
        'cart_total_cost': total_cost
    }