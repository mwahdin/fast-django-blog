# 🚀 Django Blog

## سیستم وبلاگ پیشرفته جنگو (Hybrid Architecture: CBV + DRF)

یک پروژه آموزشی و صنعتی توسعه داده شده با **Django** و **Django REST Framework (DRF)** که با هدف یادگیری عمیق معماری جنگو، کلاس‌بیس ویوها (CBV)، توسعه API و پیاده‌سازی زیرساخت‌های مدرن بک‌اند طراحی شده است.

این پروژه از معماری **Hybrid Backend** بهره می‌برد؛ به این معنا که هم رابط کاربری مبتنی بر قالب‌های HTML جنگو را ارائه می‌دهد و هم یک لایه API مستقل برای استفاده در اپلیکیشن‌های موبایل و فرانت‌اندهای مدرن فراهم می‌کند.

---

# ✨ Features

## 👤 Accounts & Authentication

### Custom User Model

سیستم احراز هویت پروژه به صورت کامل بر پایه ایمیل طراحی شده و وابستگی به فیلد پیش‌فرض `username` حذف شده است. این رویکرد ساختاری مدرن‌تر برای مدیریت کاربران فراهم می‌کند و فرآیند ورود و ثبت‌نام را برای کاربران ساده‌تر می‌سازد.

### Profile Management

به منظور جداسازی مسئولیت‌ها و افزایش انعطاف‌پذیری، اطلاعات اصلی کاربر و اطلاعات پروفایل در مدل‌های مجزا ذخیره می‌شوند. این ساختار توسعه قابلیت‌های آینده مانند شبکه اجتماعی، داشبورد کاربری و تنظیمات شخصی را آسان‌تر می‌کند.

### Signals Integration

با استفاده از سیگنال `post_save`، پروفایل هر کاربر به صورت خودکار پس از ثبت‌نام ایجاد می‌شود. این مکانیزم از ایجاد داده‌های ناقص جلوگیری کرده و یکپارچگی اطلاعات کاربران را تضمین می‌کند.

---

## 📝 Blog & Content Management

### SEO-Friendly URLs

برای دسترسی به صفحات جزئیات مقالات از فیلد `slug` به جای شناسه عددی استفاده شده است. این رویکرد باعث تولید URLهای خواناتر و سازگارتر با استانداردهای سئو می‌شود و تجربه کاربری بهتری فراهم می‌کند.

### Article Status Management

مدیریت وضعیت انتشار مقالات با استفاده از `TextChoices` پیاده‌سازی شده است. این ساختار امکان کنترل چرخه انتشار محتوا را فراهم کرده و خوانایی و نگهداری کد را بهبود می‌بخشد.

**وضعیت‌های فعلی:**

* Draft (DR)
* Published (PB)

### Category System

مقالات در دسته‌بندی‌های مختلف سازمان‌دهی می‌شوند و اسلاگ هر دسته‌بندی به صورت خودکار در پنل مدیریت تولید می‌شود. این قابلیت مدیریت محتوا را ساده‌تر کرده و ساختار منظم‌تری برای وبلاگ ایجاد می‌کند.

### Content Presentation

نمایش مقالات با استفاده از `ListView` و `DetailView` پیاده‌سازی شده است. بهره‌گیری از کلاس‌بیس ویوها باعث کاهش کدهای تکراری و افزایش قابلیت توسعه و نگهداری پروژه شده است.

---

## 🏗 Backend Architecture

### Hybrid Backend

پروژه به صورت همزمان شامل رابط کاربری مبتنی بر قالب‌های جنگو و یک لایه API مستقل است. این معماری امکان استفاده از پروژه به عنوان Backend اپلیکیشن‌های موبایل، SPAها و سایر سرویس‌های مدرن را فراهم می‌کند.

### PostgreSQL Integration

برای ذخیره‌سازی داده‌ها از PostgreSQL استفاده شده است؛ یکی از قدرتمندترین پایگاه‌های داده متن‌باز که در بسیاری از پروژه‌های سازمانی و محیط‌های Production مورد استفاده قرار می‌گیرد.

### Redis Integration

زیرساخت Redis از ابتدا در پروژه آماده شده است تا در مراحل توسعه برای کشینگ، مدیریت Sessionها و پردازش وظایف ناهمگام با Celery مورد استفاده قرار گیرد.

### Dockerized Infrastructure

تمام سرویس‌های پروژه شامل Django، PostgreSQL و Redis در کانتینرهای مستقل اجرا می‌شوند. این رویکرد فرآیند توسعه، استقرار و همکاری تیمی را ساده‌تر و قابل پیش‌بینی‌تر می‌کند.

---

## 🌍 Internationalization

تمام رشته‌های متنی پروژه با استفاده از `gettext_lazy` آماده ترجمه‌سازی شده‌اند. این قابلیت امکان چندزبانه کردن پروژه و توسعه آن برای کاربران بین‌المللی را فراهم می‌کند.

---

## 📂 Media & Static Files

مدیریت فایل‌های رسانه‌ای و استاتیک پروژه به صورت کامل پیکربندی شده است. کاربران می‌توانند تصاویر پروفایل و تصاویر مقالات را بارگذاری کرده و در محیط توسعه به صورت زنده مشاهده کنند.

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

این دستور سرویس‌های زیر را به صورت همزمان راه‌اندازی می‌کند:

* Django Web Application
* PostgreSQL Database
* Redis Server

---

## 3. Apply Migrations

```bash
docker compose run web python manage.py makemigrations
docker compose run web python manage.py migrate
```

این دستورات جداول مورد نیاز پروژه را در پایگاه داده PostgreSQL ایجاد می‌کنند.

---

## 4. Create Superuser

```bash
docker compose run web python manage.py createsuperuser
```

برای دسترسی به پنل مدیریت جنگو، یک کاربر ادمین ایجاد کنید.

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

این پروژه با هدف تبدیل شدن به یک پلتفرم وبلاگ‌نویسی مدرن، مقیاس‌پذیر و API-Driven در حال توسعه است. امکانات فعلی و برنامه‌های آینده پروژه در فازهای زیر دسته‌بندی شده‌اند.

## ✅ Phase 1 — Infrastructure & Core Models

* [x] Docker Multi-Container Architecture
* [x] PostgreSQL Integration
* [x] Redis Integration
* [x] Custom User Model
* [x] Automatic Profile Creation via Signals
* [x] Category & Post Models
* [x] TextChoices Status System
* [x] Slug-Based Routing
* [x] ListView Implementation
* [x] DetailView Implementation

---

## 🚧 Phase 2 — Content Management & API

تمرکز این فاز بر توسعه سیستم مدیریت محتوا و تکمیل لایه API پروژه است.

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

هدف این فاز نزدیک کردن پروژه به قابلیت‌های مورد انتظار از یک وبلاگ مدرن و آماده استفاده در محیط واقعی است.

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

این پروژه صرفاً یک وبلاگ ساده نیست؛ بلکه به عنوان بستری برای یادگیری و پیاده‌سازی مفاهیم مهم توسعه بک‌اند طراحی شده است.

مهم‌ترین اهداف پروژه عبارت‌اند از:

* تسلط بر Django CBVs
* طراحی Custom User Model
* کار با Django ORM
* مدیریت Authentication و Authorization
* استفاده از Django Signals
* توسعه API با Django REST Framework
* کار با PostgreSQL و Redis
* پیاده‌سازی Dockerized Applications
* طراحی معماری‌های مقیاس‌پذیر برای پروژه‌های واقعی

---

# 📄 License

This project is developed for educational and portfolio purposes.
