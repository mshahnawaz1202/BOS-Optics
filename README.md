# 👓 BOS Optics

> **A modern, full-stack Django eyewear e-commerce platform featuring premium UI, shopping cart, checkout, user authentication, blog, and appointment booking.**

<p align="center">

![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

## 📖 Overview

**BOS Optics** is a modern and responsive optical e-commerce platform built with **Django**. The project provides customers with a premium shopping experience while enabling administrators to efficiently manage products, categories, appointments, blog posts, orders, testimonials, FAQs, and newsletters through the Django Admin Dashboard.

It demonstrates best practices in Django development, including modular application architecture, authentication, CRUD operations, session management, and responsive frontend design.

---

# ✨ Features

## 🏠 Home

- Premium Hero Banner
- Featured Categories
- Product Tabs
- Services Section
- Brand Showcase
- Promotional Banner
- Customer Testimonials
- Statistics Counter
- Latest Blog
- Newsletter Subscription
- Instagram Gallery
- Contact Section
- Frequently Asked Questions

---

## 🛍 Shop

- Product Listing
- Product Categories
- Search Products
- Product Details
- Related Products

---

## 🛒 Shopping Cart

- Session-Based Cart
- Update Quantity
- Remove Items
- Checkout
- Order Confirmation

---

## 👤 User Accounts

- Register
- Login
- Logout
- User Profile
- Order History

---

## 📝 Blog

- Blog Listing
- Blog Details
- Latest Articles

---

## 👁 Services

- Book Eye Examination
- Consultation Requests
- Appointment Scheduling

---

## ⚙️ Admin Dashboard

Manage:

- Products
- Categories
- Brands
- Orders
- Customers
- Blog Posts
- FAQs
- Testimonials
- Appointments
- Newsletter Subscribers

---

# 🛠️ Tech Stack

| Technology      | Description               |
| --------------- | ------------------------- |
| 🐍 Python 3.14+ | Programming Language      |
| 🌿 Django 6.0   | Backend Framework         |
| 🗄 SQLite       | Development Database      |
| 🎨 HTML5        | Markup                    |
| 💎 CSS3         | Styling                   |
| ⚡ JavaScript   | Client-side Interactivity |

---

# 📂 Project Structure

```text
BOS-Optics/
│
├── bosoptics/              # Django project configuration
│
├── core/                   # Home, Authentication, Profile
│
├── products/               # Products, Categories, Cart & Orders
│
├── blog/                   # Blog System
│
├── services/               # Appointment Booking
│
├── templates/              # HTML Templates
│
├── static/                 # CSS, JS, Images
│
├── media/                  # Uploaded Media
│
├── manage.py
│
├── requirements.txt
│
└── README.md
```

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/mshahnawaz1202/BOS-Optics.git

cd BOS-Optics
```

---

## 2️⃣ Install Dependencies

```bash
uv sync
```

---

## 3️⃣ Apply Database Migrations

```bash
uv run python manage.py migrate
```

---

## 4️⃣ Populate Sample Data

```bash
uv run python manage.py seed_home_data
```

---

## 5️⃣ Create Superuser

```bash
uv run python manage.py createsuperuser
```

---

## 6️⃣ Start Development Server

```bash
uv run python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

# 🌐 Application Routes

| Page                | URL                     |
| ------------------- | ----------------------- |
| 🏠 Home             | `/home/`              |
| 🛍 Shop             | `/products/`          |
| 🛒 Cart             | `/products/cart/`     |
| 💳 Checkout         | `/products/checkout/` |
| 📝 Blog             | `/blog/`              |
| 👁 Book Appointment | `/services/book/`     |
| 🔐 Login            | `/home/login/`        |
| 📝 Register         | `/home/register/`     |
| 👤 My Profile       | `/home/profile/`      |
| ⚙️ Django Admin   | `/admin/`             |

---

# 📸 Screenshots

> Add your screenshots inside the `docs/screenshots` folder.

```text
docs/
└── screenshots/
    ├── home.png
    ├── products.png
    ├── blog.png
    ├── checkout.png
    ├── profile.png
    └── admin.png
```

Example:

```md
![Home Page](docs/screenshots/home.png)

![Products](docs/screenshots/products.png)
```

---

# 🌟 Future Improvements

- 💳 Stripe Payment Integration
- ❤️ Wishlist
- ⭐ Product Reviews & Ratings
- 🎁 Coupons & Discounts
- 📧 Email Notifications
- 📦 Inventory Management
- 🤖 AI Product Recommendations
- 🔍 Advanced Search & Filters
- 🌍 Multi-language Support
- 🌙 Dark Mode

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/NewFeature
```

3. Commit your changes

```bash
git commit -m "Add New Feature"
```

4. Push the branch

```bash
git push origin feature/NewFeature
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Muhammad Shah Nawaz

**Software Engineer**

- 🌐 GitHub: https://github.com/mshahnawaz1202
- 💼 LinkedIn: https://linkedin.com/in/muhammad-shah-nawaz-se

---

<div align="center">

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

| Page             | URL                     |
| ---------------- | ----------------------- |
| Home             | `/home/`              |
| Shop             | `/products/`          |
| Cart             | `/products/cart/`     |
| Checkout         | `/products/checkout/` |
| Blog             | `/blog/`              |
| Book Appointment | `/services/book/`     |
| Login            | `/home/login/`        |
| Register         | `/home/register/`     |
| My Account       | `/home/profile/`      |
| Admin            | `/admin/`             |

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
