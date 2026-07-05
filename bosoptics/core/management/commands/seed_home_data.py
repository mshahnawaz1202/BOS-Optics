from decimal import Decimal

from django.core.management.base import BaseCommand

from blog.models import Post
from core.models import FAQ, Statistic, Testimonial
from products.models import Brand, Category, Product
from services.models import Service

STATIC = '/static/core/images'


class Command(BaseCommand):
    help = 'Seed sample data for the BOS Optics home page'

    def handle(self, *args, **options):
        if Category.objects.exists():
            self.stdout.write(self.style.WARNING('Data already exists. Skipping seed.'))
            return

        categories = [
            ('Men', 'men', f'{STATIC}/angus-gray-bSjqyqukCjY-unsplash.jpg'),
            ('Women', 'women', f'{STATIC}/tamara-bellis-tw5_DJQaeDU-unsplash.jpg'),
            ('Kids', 'kids', f'{STATIC}/irene-kredenets-LaXCHG-yCJg-unsplash.jpg'),
            ('Sunglasses', 'sunglasses', f'{STATIC}/claudio-schwarz-e8TtkC5xyv4-unsplash.jpg'),
            ('Prescription', 'prescription', f'{STATIC}/giorgio-trovato-K62u25Jk6vo-unsplash.jpg'),
            ('Blue Light', 'blue-light', f'{STATIC}/jess-bailey-WeCoLo0Rxp4-unsplash.jpg'),
        ]
        cat_objs = {}
        for name, slug, img in categories:
            cat_objs[slug] = Category.objects.create(
                name=name, slug=slug, static_image=img,
                description=f'Explore our premium {name.lower()} eyewear collection.',
            )

        brands = [
            ('Ray-Ban', f'{STATIC}/g-1.png'),
            ('Oakley', f'{STATIC}/g-2.png'),
            ('Gucci', f'{STATIC}/g-3.png'),
            ('Prada', f'{STATIC}/g-4.png'),
            ('Versace', f'{STATIC}/g-5.png'),
            ('Tom Ford', f'{STATIC}/g-6.png'),
            ('Persol', f'{STATIC}/g-7.png'),
            ('Dior', f'{STATIC}/g-8.png'),
        ]
        brand_objs = {}
        for name, logo in brands:
            brand_objs[name] = Brand.objects.create(name=name, static_logo=logo)

        products_data = [
            ('Classic Black Frame', 'classic-black-frame', 99.00, 129.00, 'men', 'Ray-Ban',
             f'{STATIC}/giorgio-trovato-K62u25Jk6vo-unsplash.jpg', True, True, True),
            ('Premium Round Glasses', 'premium-round-glasses', 120.00, None, 'women', 'Gucci',
             f'{STATIC}/puneeth-shetty-bEiD43gc_lI-unsplash.jpg', True, True, False),
            ('Blue Light Glasses', 'blue-light-glasses', 79.00, 99.00, 'blue-light', 'Oakley',
             f'{STATIC}/jess-bailey-WeCoLo0Rxp4-unsplash.jpg', True, False, True),
            ('Luxury Sunglasses', 'luxury-sunglasses', 149.00, 189.00, 'sunglasses', 'Prada',
             f'{STATIC}/claudio-schwarz-e8TtkC5xyv4-unsplash.jpg', True, True, True),
            ('Urban Aviator', 'urban-aviator', 135.00, None, 'men', 'Ray-Ban',
             f'{STATIC}/dmitry-ratushny-wpi3sDUrSEk-unsplash.jpg', False, True, True),
            ('Elegant Cat-Eye', 'elegant-cat-eye', 110.00, 140.00, 'women', 'Versace',
             f'{STATIC}/logan-weaver-lgnwvr-IVXoVHXqVCY-unsplash.jpg', False, True, False),
            ('Kids Flex Frame', 'kids-flex-frame', 65.00, None, 'kids', 'Persol',
             f'{STATIC}/irene-kredenets-LaXCHG-yCJg-unsplash.jpg', False, True, False),
            ('Sport Shield', 'sport-shield', 159.00, 199.00, 'sunglasses', 'Oakley',
             f'{STATIC}/matthew-fassnacht-gLtxrJ8UQIY-unsplash.jpg', False, False, True),
        ]
        for name, slug, price, old_price, cat, brand, img, featured, new, best in products_data:
            Product.objects.create(
                name=name, slug=slug, description=f'Premium {name.lower()} from BOS Optics.',
                price=Decimal(str(price)), old_price=Decimal(str(old_price)) if old_price else None,
                category=cat_objs[cat], brand=brand_objs[brand], static_image=img,
                is_featured=featured, is_new_arrival=new, is_best_seller=best,
            )

        services = [
            ('Eye Examination', 'eye-examination', 'Comprehensive vision testing by certified optometrists.', 'eye', '1500.00', '30 mins'),
            ('Frame Fitting', 'frame-fitting', 'Personalized fitting for comfort, style, and perfect alignment.', 'frame', '500.00', '20 mins'),
            ('Lens Customization', 'lens-customization', 'Anti-glare, blue-light, progressive, and photochromic lens options.', 'lens', '2500.00', '45 mins'),
            ('Contact Lens Fitting', 'contact-lens-fitting', 'Expert fitting and trial lenses for optimal comfort.', 'eye', '1200.00', '30 mins'),
            ('Repairs & Adjustments', 'repairs-adjustments', 'Quick frame repairs, screw replacements, and alignment tweaks.', 'frame', '300.00', '15 mins'),
            ('Corporate Eye Care', 'corporate-eye-care', 'On-site eye screenings and employee vision wellness programs.', 'corporate', None, '2 hours'),
        ]
        for title, slug, desc, icon, price, duration in services:
            Service.objects.create(
                title=title, slug=slug, description=desc, icon=icon,
                price=Decimal(price) if price else None, duration=duration,
            )

        testimonials = [
            ('Ali Khan', 'Verified Buyer, Islamabad', 'Excellent quality and fast delivery! The frames fit perfectly.', 5, f'{STATIC}/client.png'),
            ('Sarah Ahmed', 'Lahore', 'Stylish frames at affordable prices. Highly recommend BOS Optics.', 5, None),
            ('Hassan Raza', 'Karachi', 'Best place for prescription glasses. Professional eye exam and great service.', 5, None),
        ]
        for name, title, comment, rating, avatar in testimonials:
            Testimonial.objects.create(
                client_name=name, client_title=title, comment=comment,
                rating=rating, static_avatar=avatar,
            )

        stats = [
            ('Happy Customers', 5000, '+', 'users', 1),
            ('Products Sold', 12000, '+', 'box', 2),
            ('Expert Opticians', 15, '+', 'award', 3),
            ('Satisfaction Rate', 98, '%', 'star', 4),
        ]
        for title, count, suffix, icon, order in stats:
            Statistic.objects.create(title=title, count=count, suffix=suffix, icon=icon, order=order)

        faqs = [
            ('How long does delivery take?', 'Standard delivery takes 3–5 business days nationwide. Express delivery is available in major cities within 1–2 days.', 1),
            ('Do you offer prescription lenses?', 'Yes. Bring your prescription or book an eye exam at our store. We offer single vision, bifocal, and progressive lenses.', 2),
            ('What is your return policy?', 'We offer a 30-day hassle-free return and exchange policy on all frames in original condition.', 3),
            ('Can I book an eye examination online?', 'Yes. Use our Book Appointment button or call us directly. Walk-ins are also welcome during business hours.', 4),
            ('Do you provide warranty on frames?', 'All frames come with a 1-year manufacturer warranty against defects. Extended warranty options are available.', 5),
            ('Which payment methods do you accept?', 'We accept cash, credit/debit cards, bank transfers, and mobile wallets including JazzCash and EasyPaisa.', 6),
        ]
        for question, answer, order in faqs:
            FAQ.objects.create(question=question, answer=answer, order=order)

        posts = [
            ('5 Tips for Choosing the Perfect Eyewear', '5-tips-perfect-eyewear',
             'Discover how to match frames to your face shape, lifestyle, and prescription needs.',
             f'{STATIC}/quality-img.jpg'),
            ('Blue Light Glasses: Do You Need Them?', 'blue-light-glasses-guide',
             'Learn how screen time affects your eyes and whether blue-light filtering lenses are right for you.',
             f'{STATIC}/jess-bailey-WeCoLo0Rxp4-unsplash.jpg'),
            ('2026 Eyewear Fashion Trends', '2026-eyewear-trends',
             'From oversized frames to minimalist metal designs — stay ahead with this season\'s top styles.',
             f'{STATIC}/tamara-bellis-tw5_DJQaeDU-unsplash.jpg'),
        ]
        for title, slug, excerpt, img in posts:
            Post.objects.create(
                title=title, slug=slug, excerpt=excerpt,
                content=f'{excerpt} Visit BOS Optics for expert advice and premium collections.',
                static_image=img,
            )

        self.stdout.write(self.style.SUCCESS('Home page sample data seeded successfully.'))
