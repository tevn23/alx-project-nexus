# ALX Project Nexus - Multi-Module Development Platform

A comprehensive repository showcasing diverse backend development projects, documentation, and learning resources from various technology domains including e-commerce, frontend engineering, and data science.

## 🎯 Repository Overview

This repository serves as a central hub containing:

1. **Digital Marketplace Backend** - A production-ready Django REST API for digital product marketplace
2. **Learning Documentation** - In-depth guides on software development best practices
3. **Technical Resources** - Code examples, patterns, and architectural solutions

---

## 📦 Digital Marketplace Backend

### Project Description

Digital Marketplace is a sophisticated Django REST Framework backend system designed for managing a digital product marketplace. Unlike traditional e-commerce platforms, this system is optimized for digital goods including software, courses, digital assets, and services.

### Key Differentiators

- **Digital Product Focus**: Specialized for instant delivery and license management
- **Creator Dashboard**: Tools for digital creators to manage their products
- **Subscription Support**: Recurring billing for subscription-based digital services
- **License Management**: Built-in licensing and product key generation
- **Advanced Analytics**: Detailed sales and customer analytics
- **Multi-tenant Support**: Support for multiple seller accounts

### 🚀 Features

#### Core Functionality
- ✅ **Product Management**: Create, manage, and publish digital products
- ✅ **User Authentication**: Secure JWT-based authentication with OAuth2 support
- ✅ **Order & Payment Processing**: Complete transaction flow with webhook support
- ✅ **License Generation**: Automatic license key generation and delivery
- ✅ **Download Management**: Secure download links with expiration
- ✅ **Customer Reviews**: Product ratings and review system
- ✅ **Refund Management**: Automated refund processing
- ✅ **Creator Payouts**: Payment aggregation and payout system

#### Advanced Features
- 🔒 **API Security**: Rate limiting, DDoS protection, and request signing
- 📊 **Analytics Dashboard**: Sales, user behavior, and performance metrics
- 🔔 **Notifications**: Real-time email and SMS notifications
- 🌐 **Internationalization**: Multi-language and multi-currency support
- 🔄 **Webhook System**: Real-time event notifications
- 📱 **Mobile API**: Optimized endpoints for mobile clients

### 🛠 Technologies Used

#### Backend Stack
```
Framework: Django 4.2.8
API Framework: Django REST Framework 3.14.0
Authentication: JWT (PyJWT 2.8.1)
Database: PostgreSQL with SQLite fallback
Async Tasks: Celery 5.3.4
Search: Elasticsearch (optional)
```

#### Additional Tools
```
API Documentation: drf-spectacular 0.26.5
CORS Support: django-cors-headers 4.3.0
File Handling: Pillow 10.1.0, Cloudinary 1.36.0
Production Server: Gunicorn 21.2.0
Static Files: WhiteNoise 6.6.0
Environment Management: python-decouple 3.8
```

### 📋 API Endpoints Overview

#### Products
```
GET /api/v1/products/                    # List all products
POST /api/v1/products/                   # Create new product
GET /api/v1/products/{id}/               # Get product details
PUT /api/v1/products/{id}/               # Update product
DELETE /api/v1/products/{id}/            # Delete product
GET /api/v1/products/{id}/downloads/     # Get download link
```

#### Orders
```
GET /api/v1/orders/                      # List user orders
POST /api/v1/orders/                     # Create new order
GET /api/v1/orders/{id}/                 # Get order details
POST /api/v1/orders/{id}/refund/        # Request refund
GET /api/v1/orders/{id}/receipt/        # Download receipt
```

#### Authentication
```
POST /api/v1/auth/register/              # User registration
POST /api/v1/auth/login/                 # User login
POST /api/v1/auth/refresh/               # Refresh token
GET /api/v1/auth/profile/                # Get user profile
PUT /api/v1/auth/profile/                # Update profile
POST /api/v1/auth/change-password/       # Change password
```

#### Payments
```
POST /api/v1/payments/initiate/          # Start payment process
POST /api/v1/payments/webhook/           # Payment provider webhook
GET /api/v1/payments/{id}/status/        # Check payment status
```

### 🔧 Setup & Installation

#### Prerequisites
- Python 3.10 or higher
- PostgreSQL 12+ (recommended) or SQLite
- Redis (for Celery tasks)
- Node.js (optional, for frontend)

#### Installation Steps

1. **Clone Repository**
```bash
git clone https://github.com/yourusername/alx-project-nexus.git
cd alx-project-nexus/digital_marketplace
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Environment**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Run Migrations**
```bash
python manage.py migrate
python manage.py createsuperuser
```

6. **Start Development Server**
```bash
python manage.py runserver
```

7. **Access API Documentation**
- Swagger UI: http://localhost:8000/api/docs/
- ReDoc: http://localhost:8000/api/redoc/

### 📚 Project Structure

```
digital_marketplace/
├── manage.py                 # Django management script
├── requirements.txt          # Project dependencies
├── .env.example             # Environment variables template
├── digital_marketplace/      # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── celery.py            # Celery configuration
├── apps/
│   ├── products/            # Product management
│   ├── orders/              # Order processing
│   ├── payments/            # Payment handling
│   ├── users/               # User management
│   ├── licenses/            # License generation
│   └── analytics/           # Analytics & reporting
└── tests/                   # Test suite
```

### 🚀 Deployment

#### Using Render
```bash
# Push to repository
git push origin main

# Create new service on Render dashboard
# Set environment variables
# Deploy from Git repository
```

#### Using Docker
```bash
# Build image
docker build -t digital-marketplace .

# Run container
docker run -p 8000:8000 digital-marketplace
```

### 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run with coverage
coverage run --source='.' manage.py test
coverage report

# Run specific test
python manage.py test apps.products.tests
```

### 📖 Documentation & Learning Resources

This repository also contains comprehensive documentation on:

- Software development best practices
- API design patterns
- Authentication strategies
- Performance optimization
- Testing strategies
- Deployment strategies

### 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

### 🔗 Related Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [JWT Authentication](https://tools.ietf.org/html/rfc7519)

### 👤 Author

**Mabula Thakgatso Tevin**
- GitHub: [@tevn23](https://github.com/tevn23)
- Email: mabulatt23@gmail.com

### 📅 Last Updated

December 2025

---

---

## 🚀 Digital Marketplace - Django REST API Backend

A modern Django REST Framework implementation of a digital product marketplace platform.

### Project Structure

```
digital_marketplace/
├── digital_marketplace/          # Django project configuration
│   ├── settings.py              # Django settings
│   ├── urls.py                  # Main URL routing
│   ├── wsgi.py                  # WSGI configuration
│   └── __init__.py              # Package initialization
├── apps/                        # Django applications package
│   ├── __init__.py
│   └── products/                # Products application
│       ├── models.py            # Product model definition
│       ├── serializers.py       # DRF serializers
│       ├── views.py             # ViewSet implementation
│       ├── urls.py              # App URL routing
│       ├── admin.py             # Django admin configuration
│       ├── apps.py              # App configuration
│       └── __init__.py
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

### Key Features

- **Products Management**: Complete CRUD API for digital products
- **REST API**: Fully functional REST API with DRF
- **Admin Interface**: Django admin for product management
- **Scalable Architecture**: Modular app structure for easy expansion

### Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

### API Endpoints

- `GET /api/products/` - List all products
- `POST /api/products/` - Create new product
- `GET /api/products/{id}/` - Retrieve product details
- `PUT /api/products/{id}/` - Update product
- `DELETE /api/products/{id}/` - Delete product

### Future Enhancements

- Orders management app
- User authentication and authorization
- Payment processing integration
- Review and rating system
- Advanced search and filtering

---

## ⚙️ Phase 1: Database & Configuration Setup (COMPLETED)

This phase includes all database and configuration steps needed to run the project locally.

### Phase 1 Completion Checklist ✅

- [x] **Environment Variables** - `.env.example` created with all necessary configuration templates
- [x] **Django Settings Updated** - `ProductsConfig` registered in `INSTALLED_APPS`
- [x] **URL Routing Configured** - Products app URLs wired into main Django configuration
- [x] **Git Ignore Setup** - `.gitignore` configured for Python, virtual environments, and sensitive files

### Setup Instructions for Local Development

#### 1. Clone the Repository
```bash
git clone https://github.com/tevn23/alx-project-nexus.git
cd alx-project-nexus/digital_marketplace
```

#### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
# Install all required packages
pip install -r requirements.txt
```

#### 4. Configure Environment Variables
```bash
# Copy example file and customize
cp .env.example .env

# Edit .env with your settings (use any text editor)
# Important: Change SECRET_KEY for production
```

#### 5. Run Migrations
```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate
```

#### 6. Create Superuser (Admin)
```bash
# Create Django admin user
python manage.py createsuperuser

# Follow prompts to set username, email, and password
```

#### 7. Run Development Server
```bash
# Start Django development server
python manage.py runserver

# Server will be available at http://127.0.0.1:8000/
```

#### 8. Test the API
```bash
# Access Django admin
http://127.0.0.1:8000/admin/

# Access API endpoints
http://127.0.0.1:8000/api/products/
http://127.0.0.1:8000/api/products/docs/  # Swagger docs (if configured)
```

### Database Choices

#### For Development (Recommended for beginners):
```bash
# SQLite (default) - already configured
# No additional setup needed, database is created in db.sqlite3
```

#### For Production/Advanced (Optional):
```bash
# PostgreSQL - Update .env:
DB_ENGINE=postgresql
DB_NAME=digital_marketplace
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

# Then install:
pip install psycopg2-binary
```

### Project Structure After Phase 1

```
digital_marketplace/
├── digital_marketplace/             # Django project config (Phase 1 ✅)
│   ├── settings.py                 # Django settings with INSTALLED_APPS
│   ├── urls.py                     # URL routing configured
│   ├── wsgi.py
│   └── __init__.py
├── apps/                           # Django apps package
│   ├── products/                   # Products app (Phase 1 ✅)
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py                 # Wired into main config
│   │   ├── admin.py
│   │   ├── apps.py
│   │   └── __init__.py
│   └── __init__.py
├── manage.py                       # Django management
├── requirements.txt                # Phase 1 ✅
├── .env.example                    # Phase 1 ✅
├── .gitignore                      # Phase 1 ✅
└── db.sqlite3                      # Created after migrations
```

### Troubleshooting

**Issue: `ModuleNotFoundError: No module named 'django'`**
- Solution: Ensure virtual environment is activated and run `pip install -r requirements.txt`

**Issue: `django.db.utils.OperationalError: no such table`**
- Solution: Run migrations: `python manage.py migrate`

**Issue: Port 8000 already in use**
- Solution: Run on different port: `python manage.py runserver 8001`

### Next Steps (Phase 2)
- Write comprehensive tests for the API
- Test API endpoints with Postman or Insomnia
- Implement error handling and validation



**Happy Coding! 🚀**
