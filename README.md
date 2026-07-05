# BOS Optics

A full-stack Django eyewear e-commerce website with premium UI, shopping cart, checkout, user accounts, blog, and appointment booking.

## Features

- **Home page** — Hero, categories, product tabs, services, brands, promo banner, testimonials, stats, blog, newsletter, Instagram gallery, contact, FAQ
- **Shop** — Product listing with category filters and search, product detail pages
- **Cart & Checkout** — Session-based cart, order placement, order confirmation
- **User accounts** — Register, login, logout, profile with order history
- **Blog** — Article listing and detail pages
- **Services** — Book eye exams and consultations
- **Admin panel** — Manage products, orders, blog posts, FAQs, testimonials, appointments

## Tech Stack

- Python 3.14+
- Django 6.0
- SQLite (development)
- HTML / CSS / JavaScript

## Quick Start

```bash
cd bosoptics
uv sync
uv run python manage.py migrate
uv run python manage.py seed_home_data
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

## URLs

| Page | URL |
|------|-----|
| Home | `/home/` |
| Shop | `/products/` |
| Cart | `/products/cart/` |
| Checkout | `/products/checkout/` |
| Blog | `/blog/` |
| Book Appointment | `/services/book/` |
| Login | `/home/login/` |
| Register | `/home/register/` |
| My Account | `/home/profile/` |
| Admin | `/admin/` |

## Project Structure

```
bosoptics/
├── core/           # Home, auth, profile, newsletter, FAQs
├── products/       # Products, categories, brands, cart, orders
├── blog/           # Blog posts
├── services/       # Eye care services & appointments
├── templates/      # Base layout & shared partials
└── bosoptics/      # Django settings & URLs
```

## Admin

Create a superuser and manage all content at `/admin/`:

```bash
uv run python manage.py createsuperuser
```

## Seed Data

Populate sample products, categories, blog posts, and more:

```bash
uv run python manage.py seed_home_data
```
