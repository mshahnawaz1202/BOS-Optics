from decimal import Decimal

from .models import Product

CART_SESSION_KEY = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_KEY)
        if cart is None:
            cart = self.session[CART_SESSION_KEY] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        pid = str(product.id)
        if pid in self.cart:
            self.cart[pid]['quantity'] += quantity
        else:
            self.cart[pid] = {'quantity': quantity}
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        pid = str(product.id)
        if pid in self.cart:
            del self.cart[pid]
            self.save()

    def update(self, product, quantity):
        pid = str(product.id)
        if quantity <= 0:
            self.remove(product)
        elif pid in self.cart:
            self.cart[pid]['quantity'] = quantity
            self.save()

    def clear(self):
        self.session[CART_SESSION_KEY] = {}
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        product_map = {str(p.id): p for p in products}
        for pid, item in self.cart.items():
            product = product_map.get(pid)
            if product:
                yield {
                    'product': product,
                    'quantity': item['quantity'],
                    'subtotal': product.price * item['quantity'],
                }

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total(self):
        total = Decimal('0')
        for item in self:
            total += item['subtotal']
        return total

    def is_empty(self):
        return len(self.cart) == 0