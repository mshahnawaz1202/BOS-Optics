# 👓 BOS Optics

<div align="center">

### Premium Eyewear E-Commerce Platform Built with Django

A modern, responsive, and scalable full-stack e-commerce web application for an optical store, built with Django.

<p>

![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![uv](https://img.shields.io/badge/uv-Package_Manager-6A5ACD?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

</p>

</div>

---

# 📖 Overview

**BOS Optics** is a full-stack Django e-commerce platform developed for an optical store. It enables customers to browse premium eyewear, search products, manage shopping carts, place orders, book eye-care appointments, and read informative blog posts.

The project follows a modular Django architecture using multiple reusable applications and includes a powerful Django Admin dashboard for complete website management.

---

# ✨ Features

## 🏠 Home

- Responsive landing page
- Hero section
- Featured categories
- Featured products
- Promotional banners
- Customer testimonials
- Newsletter subscription
- FAQ section
- Contact section

## 🛍️ Shop

- Product listing
- Category filtering
- Product search
- Product details
- Related products

## 🛒 Shopping

- Session-based shopping cart
- Add to cart
- Update quantity
- Remove items
- Checkout
- Order confirmation

## 👤 User Accounts

- User Registration
- Login
- Logout
- User Profile
- Order History

## 📝 Blog

- Blog listing
- Blog details
- Latest articles

## 👓 Services

- Eye examination booking
- Consultation requests
- Appointment scheduling

## ⚙️ Admin Dashboard

- Product Management
- Category Management
- Order Management
- Blog Management
- Appointment Management
- Newsletter Management
- Testimonials
- FAQs

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|----------|
| 🐍 Python | Programming Language |
| 🌿 Django | Backend Framework |
| ⚡ uv | Python Package Manager |
| 🗄 SQLite | Database |
| 🎨 HTML5 | Markup |
| 🎨 CSS3 | Styling |
| ⚡ JavaScript | Client-side Interactivity |

---

# 🏗 Project Architecture

```
User
   │
   ▼
HTML • CSS • JavaScript
   │
   ▼
Django Framework
   │
 ┌──────────────┬──────────────┬──────────────┐
 ▼              ▼              ▼
Core        Products        Blog
   │
   └──────────────┬──────────────┘
                  ▼
             Services
                  │
                  ▼
             SQLite Database
```

---

# 📂 Project Structure

```
BOS-Optics/
│
├── bosoptics/
│   ├── bosoptics/
│   ├── core/
│   ├── products/
│   ├── blog/
│   ├── services/
│   ├── templates/
│   ├── static/
│   ├── media/
│   ├── manage.py
│   └── requirements.txt
│
├── README.md
├── pyproject.toml
└── uv.lock
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/mshahnawaz1202/BOS-Optics.git
```

```bash
cd BOS-Optics/bosoptics
```

## Install Dependencies

```bash
uv sync
```

## Apply Migrations

```bash
python manage.py migrate
```

## Seed Sample Data

```bash
python manage.py seed_home_data
```

## Create Superuser

```bash
python manage.py createsuperuser
```

## Run Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000/
```

---

# 🌐 Application Routes

| Page | URL |
|------|------|
| Home | `/home/` |
| Shop | `/products/` |
| Product Details | `/products/<id>/` |
| Cart | `/products/cart/` |
| Checkout | `/products/checkout/` |
| Blog | `/blog/` |
| Book Appointment | `/services/book/` |
| Login | `/home/login/` |
| Register | `/home/register/` |
| Profile | `/home/profile/` |
| Admin | `/admin/` |

---

# 📸 Screenshots

Add screenshots of:

- Home Page
- Shop
- Product Details
- Cart
- Checkout
- Blog
- Appointment Booking
- Admin Dashboard

---

# 🚀 Future Improvements

- Stripe Payment Integration
- Wishlist
- Product Reviews
- Ratings
- Coupons
- Inventory Management
- Email Notifications
- PostgreSQL
- Docker
- REST API
- Product Filtering
- Search Suggestions

---

# 👨‍💻 Developers

### Muhammad Shah Nawaz

- GitHub: https://github.com/mshahnawaz1202
- LinkedIn: https://www.linkedin.com/in/muhammad-shah-nawaz-se

### Haider Abbas

- Team Member & Co-Developer

---

# 🤝 Contributing

Contributions, ideas, and suggestions are always welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

<div align="center">

### ⭐ If you found this project helpful, please consider giving it a star!

Built with ❤️ using Python, Django, and uv.

</div>
