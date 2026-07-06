<<<<<<< HEAD

<div align="center">

---

# 📖 Overview

**BOS Optics** is a modern full-stack **Django** application developed for an optical store. It delivers a premium online shopping experience where users can browse products, search collections, manage their shopping cart, complete purchases, book eye-care appointments, and read informative blog articles. The application also includes a comprehensive Django Admin dashboard for managing products, categories, orders, appointments, testimonials, FAQs, newsletters, and blog content.

---

=======
<div align="center">

# 👓 BOS Optics

### Premium Eyewear E-Commerce Platform Built with Django

*A modern, scalable, and responsive eyewear e-commerce platform built with Django, offering a premium shopping experience, secure authentication, shopping cart, checkout, appointment booking, blogging, and an intuitive admin dashboard.*

<p>

![Python](https://img.shields.io/badge/Python-3.14+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django)
![uv](https://img.shields.io/badge/uv-Package_Manager-DE5FE9?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

<br>

![GitHub stars](https://img.shields.io/github/stars/mshahnawaz1202/BOS-Optics?style=social)
![GitHub forks](https://img.shields.io/github/forks/mshahnawaz1202/BOS-Optics?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/mshahnawaz1202/BOS-Optics)

</p>

</div>

---

# 📖 Overview

**BOS Optics** is a modern full-stack **Django** application developed for an optical store. It delivers a premium online shopping experience where users can browse products, search collections, manage their shopping cart, complete purchases, book eye-care appointments, and read informative blog articles. The application also includes a comprehensive Django Admin dashboard for managing products, categories, orders, appointments, testimonials, FAQs, newsletters, and blog content.

---

>>>>>>> b7d7e852e8cf881fb5c0d90649c23795cf3acb36
# ✨ Features

## 🏠 Home

- Premium Hero Banner
- Featured Categories
- Featured Products
- Product Collections
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

## 🛍️ Shop

- Product Listing
- Product Categories
- Product Search
- Product Details
- Related Products

## 🛒 Shopping

- Session-Based Shopping Cart
- Add to Cart
- Update Cart
- Checkout
- Order Confirmation

## 👤 User Accounts

- Register
- Login
- Logout
- User Profile
- Order History

## 📝 Blog

- Blog Listing
- Blog Details
- Latest Articles

## 👁️ Eye Care Services

- Eye Examination Booking
- Consultation Requests
- Appointment Scheduling

## ⚙️ Admin Dashboard

- Product Management
- Category Management
- Brand Management
- Order Management
- Blog Management
- FAQ Management
- Appointment Management
- Newsletter Management
- Testimonials Management

---

# 🛠️ Tech Stack

<<<<<<< HEAD
| Technology      | Description            |
| --------------- | ---------------------- |
| 🐍 Python 3.14+ | Programming Language   |
| 🌿 Django 6.0   | Web Framework          |
| ⚡ uv           | Python Package Manager |
| 🗄 SQLite       | Development Database   |
| 🎨 HTML5        | Markup                 |
| 🎨 CSS3         | Styling                |
| ⚡ JavaScript   | Frontend Interactivity |
=======
| Technology | Description |
|------------|-------------|
| 🐍 Python 3.14+ | Programming Language |
| 🌿 Django 6.0 | Web Framework |
| ⚡ uv | Python Package Manager |
| 🗄 SQLite | Development Database |
| 🎨 HTML5 | Markup |
| 🎨 CSS3 | Styling |
| ⚡ JavaScript | Frontend Interactivity |
>>>>>>> b7d7e852e8cf881fb5c0d90649c23795cf3acb36

---

# 🏗️ Project Architecture

```text
                    User
                      │
                      ▼
           HTML • CSS • JavaScript
                      │
                      ▼
                Django Framework
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
      Core        Products        Blog
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                 Services App
                      │
                      ▼
                SQLite Database
```

---

# 📂 Project Structure

```text
BOS-Optics/
│
├── bosoptics/              # Django project configuration
├── core/                   # Home, Authentication & Profile
├── products/               # Products, Categories, Cart & Orders
├── blog/                   # Blog System
├── services/               # Appointment Booking
├── templates/              # HTML Templates
├── static/                 # CSS, JavaScript & Images
├── media/                  # Uploaded Media
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/mshahnawaz1202/BOS-Optics.git
cd BOS-Optics
```

## Install Dependencies

```bash
uv sync
```

## Apply Migrations

```bash
uv run python manage.py migrate
```

## Seed Sample Data

```bash
uv run python manage.py seed_home_data
```

## Create Superuser

```bash
uv run python manage.py createsuperuser
```

## Run Development Server

```bash
uv run python manage.py runserver
```

Open your browser:

```text
http://127.0.0.1:8000/
```
<<<<<<< HEAD

---

# 🌐 Application Routes

| Page                  | URL                     |
| --------------------- | ----------------------- |
| 🏠 Home               | `/home/`              |
| 🛍️ Shop             | `/products/`          |
| 🛒 Cart               | `/products/cart/`     |
| 💳 Checkout           | `/products/checkout/` |
| 📝 Blog               | `/blog/`              |
| 👁️ Book Appointment | `/services/book/`     |
| 🔐 Login              | `/home/login/`        |
| 📝 Register           | `/home/register/`     |
| 👤 Profile            | `/home/profile/`      |
| ⚙️ Admin            | `/admin/`             |

---

# 🛣️ Future Improvements

=======

---

# 🌐 Application Routes

| Page | URL |
|------|-----|
| 🏠 Home | `/home/` |
| 🛍️ Shop | `/products/` |
| 🛒 Cart | `/products/cart/` |
| 💳 Checkout | `/products/checkout/` |
| 📝 Blog | `/blog/` |
| 👁️ Book Appointment | `/services/book/` |
| 🔐 Login | `/home/login/` |
| 📝 Register | `/home/register/` |
| 👤 Profile | `/home/profile/` |
| ⚙️ Admin | `/admin/` |

---


# 🛣️ Future Improvements

>>>>>>> b7d7e852e8cf881fb5c0d90649c23795cf3acb36
- 💳 Online Payment Integration
- ❤️ Wishlist
- ⭐ Product Ratings & Reviews
- 🎁 Coupons & Discounts
- 📧 Email Notifications
- 📦 Inventory Management
- 🤖 AI Product Recommendations
- 🔍 Advanced Search & Filters
- 🌍 Multi-language Support
- 🌙 Dark Mode
- 📱 Progressive Web App (PWA)

---

# 🤝 Contributing

Contributions are welcome.

```bash
# Fork the repository

git checkout -b feature/new-feature

git commit -m "Add new feature"

git push origin feature/new-feature
```

Then open a Pull Request.

---

# 👨‍💻 Author

**Muhammad Shah Nawaz**

Software Engineer

- 🌐 GitHub: https://github.com/mshahnawaz1202
- 💼 LinkedIn: https://linkedin.com/in/muhammad-shah-nawaz-se

---

<div align="center">
<<<<<<< HEAD
=======

### ⭐ If you found this project helpful, consider giving it a star!

Built with ❤️ using **Python**, **Django**, and **uv**.

</div>
>>>>>>> b7d7e852e8cf881fb5c0d90649c23795cf3acb36
