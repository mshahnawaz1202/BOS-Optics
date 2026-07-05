from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .cart import Cart
from .forms import CheckoutForm
from .models import Category, Order, OrderItem, Product


def product_list(request):
    products = Product.objects.select_related('category', 'brand').all()
    category_slug = request.GET.get('category')
    search = request.GET.get('q', '').strip()

    if category_slug:
        products = products.filter(category__slug=category_slug)
    if search:
        products = products.filter(name__icontains=search)

    return render(request, 'products/list.html', {
        'products': products,
        'categories': Category.objects.all(),
        'active_category': category_slug,
        'search_query': search,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product.objects.select_related('category', 'brand'), slug=slug)
    related = Product.objects.filter(category=product.category).exclude(pk=product.pk)[:4]
    return render(request, 'products/detail.html', {
        'product': product,
        'related_products': related,
    })


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product, quantity)
    messages.success(request, f'"{product.name}" added to your cart.')
    next_url = request.POST.get('next', request.META.get('HTTP_REFERER', '/products/'))
    return redirect(next_url)


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    cart.remove(product)
    messages.info(request, f'"{product.name}" removed from cart.')
    return redirect('products:cart')


def cart_update(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.update(product, quantity)
    return redirect('products:cart')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'products/cart.html', {'cart': cart})


def checkout(request):
    cart = Cart(request)
    if cart.is_empty():
        messages.warning(request, 'Your cart is empty.')
        return redirect('products:list')

    initial = {}
    if request.user.is_authenticated:
        initial = {
            'full_name': request.user.get_full_name() or request.user.username,
            'email': request.user.email,
        }

    form = CheckoutForm(request.POST or None, initial=initial)
    if request.method == 'POST' and form.is_valid():
        order = form.save(commit=False)
        order.user = request.user if request.user.is_authenticated else None
        order.total = cart.get_total()
        order.save()
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                price=item['product'].price,
            )
        cart.clear()
        messages.success(request, f'Order #{order.pk} placed successfully!')
        return redirect('products:order_success', order_id=order.pk)

    return render(request, 'products/checkout.html', {
        'cart': cart,
        'form': form,
    })


def order_success(request, order_id):
    order = get_object_or_404(Order.objects.prefetch_related('items__product'), pk=order_id)
    if request.user.is_authenticated and order.user and order.user != request.user:
        messages.error(request, 'You do not have permission to view this order.')
        return redirect('core:home')
    return render(request, 'products/order_success.html', {'order': order})
