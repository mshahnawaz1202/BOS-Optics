from django.contrib import messages
from django.shortcuts import render, redirect

from blog.models import Post
from products.models import Brand, Category, Product
from services.models import Service

from .models import FAQ, NewsletterSubscription, Statistic, Testimonial


def home(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            _, created = NewsletterSubscription.objects.get_or_create(email=email)
            if created:
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            else:
                messages.info(request, 'You are already subscribed.')
        return redirect('home')

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
    }
    return render(request, 'core/home.html', context)
