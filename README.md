# 🚀 Django Blog

## سیستم وبلاگ پیشرفته جنگو (Hybrid Architecture: CBV + DRF)

یک پروژه آموزشی و صنعتی توسعه داده شده با **Django** و **Django REST Framework (DRF)** که با هدف یادگیری عمیق معماری جنگو، کلاس‌بیس ویوها (CBV)، توسعه API و پیاده‌سازی زیرساخت‌های مدرن بک‌اند طراحی شده است.

این پروژه از معماری **Hybrid Backend** بهره می‌برد؛ به این معنا که هم رابط کاربری مبتنی بر قالب‌های HTML جنگو را ارائه می‌دهد و هم یک لایه API مستقل برای استفاده در اپلیکیشن‌های موبایل و فرانت‌اندهای مدرن فراهم می‌کند.

---

# ✨ Features

## 👤 Accounts & Authentication

### Custom User Model

* حذف کامل فیلد `username`
* احراز هویت مبتنی بر ایمیل
* استفاده از `email` به عنوان `USERNAME_FIELD`

### Profile Management

* جداسازی اطلاعات هویتی و اطلاعات پروفایل
* مدل مستقل `Profile`
* مدیریت خودکار پروفایل کاربران

### Signals Integration

* استفاده از سیگنال `post_save`
* ایجاد خودکار پروفایل هنگام ثبت‌نام کاربران

---

## 📝 Blog & Content Management

### SEO-Friendly URLs

* استفاده از `slug`
* حذف وابستگی به شناسه عددی (`pk`)
* آدرس‌های مناسب برای موتورهای جستجو

### Article Status Management

* پیاده‌سازی استاندارد `TextChoices`
* مدیریت وضعیت مقالات:

  * Draft (DR)
  * Published (PB)

### Category System

* دسته‌بندی مقالات
* تولید خودکار Slug در پنل مدیریت
* ارتباط ForeignKey بین مقالات و دسته‌بندی‌ها

### Content Presentation

* پیاده‌سازی ListView
* پیاده‌سازی DetailView
* نمایش مقالات بر اساس Slug

---

## 🏗 Backend Architecture

### Hybrid Backend

* Django Template Views (CBV)
* Django REST Framework (DRF)
* آمادگی برای اتصال به Frontendهای مدرن

### PostgreSQL Integration

* استفاده از PostgreSQL 15
* ذخیره‌سازی پایدار داده‌ها
* آماده برای محیط Production

### Redis Integration

* پیکربندی Redis 7
* آماده برای:

  * Caching
  * Session Management
  * Celery Tasks

### Dockerized Infrastructure

* Docker
* Docker Compose
* معماری Multi-Container

---

## 🌍 Internationalization

* استفاده از `gettext_lazy`
* آماده برای چندزبانه شدن پروژه
* قابلیت توسعه برای زبان‌های مختلف

---

## 📂 Media & Static Files

* مدیریت فایل‌های Media
* آپلود تصاویر پروفایل کاربران
* آپلود کاور مقالات
* مدیریت فایل‌های Static

---

# 🛠 Tech Stack

## Backend

* Django 5.x
* Django REST Framework (DRF)

## Database

* PostgreSQL 15
* Redis 7

## DevOps

* Docker
* Docker Compose

## Python Packages

* psycopg2-binary

---

# 📁 Project Structure

```text
├── core/                  # تنظیمات اصلی پروژه
├── accounts/              # مدیریت کاربران و پروفایل‌ها
├── blog/                  # مدیریت مقالات و دسته‌بندی‌ها
├── templates/             # قالب‌های HTML
├── static/                # فایل‌های استاتیک
├── media/                 # فایل‌های آپلودی
├── Dockerfile             # ساخت ایمیج پروژه
├── docker-compose.yml     # مدیریت سرویس‌ها
└── requirements.txt       # وابستگی‌های پروژه
```

---

# 🚀 Quick Start

## Prerequisites

پیش از شروع، مطمئن شوید که موارد زیر روی سیستم شما نصب شده‌اند:

* Docker
* Docker Compose

---

## 1. Clone Repository

```bash
git clone <repository-url>
cd django_blog
```

---

## 2. Build & Run Containers

```bash
docker compose up --build
```

این دستور سرویس‌های زیر را اجرا می‌کند:

* Django Web
* PostgreSQL
* Redis

---

## 3. Apply Migrations

```bash
docker compose run web python manage.py makemigrations
docker compose run web python manage.py migrate
```

---

## 4. Create Superuser

```bash
docker compose run web python manage.py createsuperuser
```

---

## 5. Access Application

### Website

```text
http://localhost:8000
```

### Django Admin

```text
http://localhost:8000/admin
```

### API

```text
http://localhost:8000/api/v1/
```

---

# 📈 Development Roadmap

## ✅ Phase 1 — Infrastructure & Core Models

* [x] Docker Multi-Container Architecture
* [x] PostgreSQL Integration
* [x] Redis Integration
* [x] Custom User Model
* [x] Automatic Profile Creation via Signals
* [x] Category & Post Models
* [x] TextChoices Status System
* [ ] Slug-Based Routing
* [ ] ListView Implementation
* [ ] DetailView Implementation

---

## 🚧 Phase 2 — Content Management & API

* [ ] CreateView for User Posts
* [ ] Custom Forms
* [ ] UpdateView
* [ ] DeleteView
* [ ] Permission Mixins
* [ ] DRF Serializers
* [ ] ViewSets
* [ ] API Authentication
* [ ] Redis Page Caching

---

## 🔥 Phase 3 — Modern Blog Features

### User Interaction

* [ ] Nested Comments System
* [ ] Reply to Comments
* [ ] Like & Reaction System
* [ ] AJAX/API-Based Interactions

### Search & Discovery

* [ ] Advanced Search
* [ ] Category Filtering
* [ ] Tag System
* [ ] Related Posts

### Reading Experience

* [ ] Reading Time Calculation
* [ ] Article View Counter
* [ ] Popular Posts Section
* [ ] Author Profile Pages

### Performance & Scalability

* [ ] Redis Query Caching
* [ ] Celery Background Tasks
* [ ] Email Queue Processing
* [ ] Rate Limiting

### Content Distribution

* [ ] RSS Feed
* [ ] Newsletter System
* [ ] Email Notifications

### Security

* [ ] API Throttling
* [ ] JWT Authentication
* [ ] CSRF & Security Hardening
* [ ] Production Deployment Configuration

---

# 🎯 Project Goals

این پروژه با هدف یادگیری و پیاده‌سازی مفاهیم زیر توسعه داده شده است:

* Django CBVs
* Django ORM
* Django Authentication System
* Django Signals
* Django REST Framework
* PostgreSQL
* Redis
* Docker & Containerization
* Scalable Backend Architecture

---

# 📄 License

This project is developed for educational and portfolio purposes.
