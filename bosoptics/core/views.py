from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from blog.models import Post
from products.models import Brand, Category, Product
from services.models import Appointment, Service

from .forms import ContactForm, LoginForm, RegisterForm
from .models import FAQ, NewsletterSubscription, Statistic, Testimonial


def home(request):
    context = {
        'categories': Category.objects.all()[:8],
        'new_arrivals': Product.objects.filter(is_new_arrival=True)[:4],
        'featured_products': Product.objects.filter(is_featured=True)[:4],
        'best_sellers': Product.objects.filter(is_best_seller=True)[:4],
        'brands': Brand.objects.all()[:8],
        'services': Service.objects.all()[:6],
        'testimonials': Testimonial.objects.all()[:6],
        'statistics': Statistic.objects.all()[:4],
        'blog_posts': Post.objects.order_by('-created_at')[:3],
        'faqs': FAQ.objects.all()[:8],
        'contact_form': ContactForm(),
    }
    return render(request, 'core/home.html', context)


def newsletter_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        next_url = request.POST.get('next', reverse('core:home'))
        if email:
            _, created = NewsletterSubscription.objects.get_or_create(email=email)
            if created:
                messages.success(request, 'Thank you for subscribing!')
            else:
                messages.info(request, 'You are already subscribed.')
        if '#newsletter' not in next_url:
            next_url += '#newsletter'
        return redirect(next_url)
    return redirect('core:home')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:home')

    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.get_user())
        messages.success(request, f'Welcome back, {request.user.get_short_name() or request.user.username}!')
        next_url = request.GET.get('next', reverse('core:home'))
        return redirect(next_url)

    return render(request, 'core/login.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('core:home')

    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Your account has been created. Welcome to BOS Optics!')
        return redirect('core:home')

    return render(request, 'core/register.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('core:home')


def privacy_policy(request):
    return render(request, 'core/legal.html', {
        'page_title': 'Privacy Policy',
        'content': (
            'BOS Optics respects your privacy. We collect only the information necessary '
            'to process orders, appointments, and newsletter subscriptions. We never sell '
            'your personal data to third parties. Contact us at support@bosoptics.com for '
            'any privacy-related inquiries.'
        ),
    })


def terms_conditions(request):
    return render(request, 'core/legal.html', {
        'page_title': 'Terms & Conditions',
        'content': (
            'By using the BOS Optics website and services, you agree to our terms of use. '
            'All products are subject to availability. Prices may change without notice. '
            'Returns are accepted within 30 days in original condition. Prescription lenses '
            'require a valid prescription from a licensed optometrist.'
        ),
    })


def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent. We will get back to you soon!')
        else:
            messages.error(request, 'Please correct the errors in the contact form.')
    return redirect(reverse('core:home') + '#contact')


@login_required
def profile(request):
    from products.models import Order
    orders = Order.objects.filter(user=request.user).prefetch_related('items__product')
    appointments = Appointment.objects.filter(email=request.user.email).select_related('service')
    return render(request, 'core/profile.html', {
        'orders': orders,
        'appointments': appointments,
    })
