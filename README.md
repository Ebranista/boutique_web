# Boutique Shop Management System - Backend API

A production-ready, enterprise-grade RESTful backend API for a Boutique Shop Management System built with Flask.

## Features

- **Authentication & Authorization**: JWT-based authentication with role-based access control (RBAC)
- **Inventory Management**: Complete product, category, and brand management with stock tracking
- **Sales & POS**: Point of sale system with cart, payment processing, and receipt generation
- **Purchases**: Supplier management and purchase order processing
- **Expenses**: Expense tracking with categories and recurring expenses
- **Capital Management**: Track business capital, investments, and withdrawals
- **Reporting**: Comprehensive reports for sales, purchases, expenses, profit, and inventory
- **Dashboard**: Real-time analytics and statistics
- **Notifications**: In-app and push notifications (Firebase integration ready)
- **Audit Trail**: Complete audit logging for all system actions
- **Barcode & QR Code**: Automatic generation for products

## Technology Stack

- **Framework**: Flask 3.0+
- **Database**: MySQL with SQLAlchemy ORM
- **Migrations**: Alembic with Flask-Migrate
- **Authentication**: Flask-JWT-Extended
- **Validation**: Marshmallow
- **API Documentation**: Flask-RESTX (Swagger/OpenAPI)
- **Environment**: python-dotenv
- **Testing**: Pytest

## Architecture

The application follows a clean, modular architecture:

```
backend/
├── app/
│   ├── auth/              # Authentication module
│   ├── users/             # User management
│   ├── dashboard/         # Dashboard analytics
│   ├── products/          # Product management
│   ├── categories/        # Category management
│   ├── brands/            # Brand management
│   ├── inventory/         # Inventory management
│   ├── suppliers/         # Supplier management
│   ├── customers/         # Customer management
│   ├── purchases/         # Purchase management
│   ├── sales/             # Sales/POS management
│   ├── expenses/          # Expense management
│   ├── reports/           # Reporting module
│   ├── notifications/     # Notification system
│   ├── settings/          # Application settings
│   ├── audit/             # Audit logging
│   ├── models/            # SQLAlchemy models
│   ├── schemas/           # Marshmallow schemas
│   ├── repositories/      # Repository pattern (data access)
│   ├── services/          # Business logic layer
│   ├── middleware/        # Authentication & authorization
│   ├── utils/             # Helper utilities
│   ├── extensions.py      # Flask extensions
│   ├── config.py          # Configuration classes
│   └── __init__.py        # Application factory
├── migrations/            # Database migrations
├── tests/                 # Unit and integration tests
├── uploads/               # File uploads
├── logs/                  # Application logs
├── requirements.txt       # Python dependencies
├── run.py                 # Application entry point
├── .env.example           # Environment variables template
└── README.md             # This file
```

## Installation

### Prerequisites

- Python 3.12+
- MySQL 8.0+
- pip

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Create database**
   ```bash
   mysql -u root -p
   CREATE DATABASE boutique_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   EXIT;
   ```

6. **Run migrations**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

7. **Seed initial data** (optional)
   ```bash
   # Create default admin user, roles, permissions, etc.
   python scripts/seed_data.py
   ```

## Running the Application

### Development

```bash
python run.py
```

The API will be available at `http://localhost:5000`

### Production

```bash
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

## API Documentation

Swagger/OpenAPI documentation is available at:
- **Swagger UI**: `http://localhost:5000/api/v1/swagger/`
- **JSON Spec**: `http://localhost:5000/api/v1/swagger.json`

## API Endpoints

### Authentication (`/api/v1/auth`)
- `POST /login` - User login
- `POST /refresh` - Refresh access token
- `POST /logout` - User logout
- `POST /change-password` - Change password
- `GET /me` - Get current user

### Users (`/api/v1/users`)
- `GET /users` - List all users
- `POST /users` - Create user
- `GET /users/<id>` - Get user details
- `PUT /users/<id>` - Update user
- `DELETE /users/<id>` - Delete user

### Products (`/api/v1/products`)
- `GET /products` - List products
- `POST /products` - Create product
- `GET /products/<id>` - Get product
- `PUT /products/<id>` - Update product
- `DELETE /products/<id>` - Delete product
- `GET /products/search` - Search products
- `GET /products/barcode/<barcode>` - Get by barcode
- `GET /products/low-stock` - Low stock products
- `GET /products/out-of-stock` - Out of stock products

### Sales (`/api/v1/sales`)
- `GET /sales` - List sales
- `POST /sales` - Create sale (POS)
- `GET /sales/<id>` - Get sale
- `POST /sales/<id>/refund` - Refund sale
- `POST /sales/<id>/cancel` - Cancel sale
- `GET /sales/today` - Today's sales
- `GET /sales/customer/<id>` - Sales by customer

### Inventory (`/api/v1/inventory`)
- `GET /inventory` - List inventory
- `GET /inventory/product/<id>` - Get by product
- `POST /inventory/adjust` - Adjust stock
- `GET /inventory/low-stock` - Low stock
- `GET /inventory/out-of-stock` - Out of stock

### Dashboard (`/api/v1/dashboard`)
- `GET /dashboard/summary` - Complete summary
- `GET /dashboard/today-stats` - Today's stats
- `GET /dashboard/monthly-stats` - Monthly stats
- `GET /dashboard/inventory-stats` - Inventory stats
- `GET /dashboard/capital` - Current capital
- `GET /dashboard/top-products` - Top selling products
- `GET /dashboard/recent-sales` - Recent sales
- `GET /dashboard/monthly-chart` - Monthly chart data

### Reports (`/api/v1/reports`)
- `GET /reports/sales` - Sales report
- `GET /reports/purchases` - Purchase report
- `GET /reports/expenses` - Expense report
- `GET /reports/inventory` - Inventory report
- `GET /reports/profit` - Profit report
- `GET /reports/product-profit` - Product profit report
- `GET /reports/customers` - Customer report
- `GET /reports/suppliers` - Supplier report

## Roles & Permissions

### Roles
- **Administrator**: Full system access
- **Manager**: Manage products, sales, purchases, expenses, view reports
- **Cashier**: Process sales, view inventory

### Permissions
- `manage_products` - Create, update, delete products
- `manage_sales` - Process sales, refunds
- `manage_purchases` - Create purchases
- `manage_expenses` - Create expenses
- `manage_users` - Manage users
- `manage_inventory` - Adjust inventory
- `view_reports` - View reports
- `manage_settings` - Update settings

## Business Rules

1. **Stock Management**
   - Stock cannot become negative
   - Every stock movement is logged
   - Low stock alerts are generated automatically

2. **Sales**
   - Selling automatically reduces stock
   - Selling automatically records profit
   - Selling automatically updates capital
   - Every sale generates a unique invoice

3. **Purchases**
   - Purchases automatically increase stock
   - Purchases update capital investment

4. **Expenses**
   - Expenses automatically reduce current capital

5. **Validation**
   - Buying price cannot exceed selling price (without admin approval)
   - Duplicate product codes/barcodes are prevented
   - Email and phone validation

## Testing

Run tests:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=app --cov-report=html
```

## Docker Support

Docker configuration is included for containerized deployment.

```bash
docker build -t boutique-backend .
docker run -p 5000:5000 boutique-backend
```

## Security Features

- JWT Authentication with access/refresh tokens
- Password hashing with bcrypt
- Role-Based Access Control (RBAC)
- Input validation with Marshmallow
- SQL Injection protection (SQLAlchemy ORM)
- XSS protection
- CSRF protection (where applicable)
- Secure headers
- Rate limiting (ready to implement)
- CORS configuration

## Logging

Application logs are stored in `logs/app.log` with JSON formatting for easy parsing.

## Audit Trail

All system actions are logged to the audit trail including:
- User actions (login, logout)
- CRUD operations on all entities
- IP address and user agent
- Timestamps
- Old and new values for updates

## Offline Synchronization

The backend supports offline synchronization for mobile apps:
- Last updated timestamps
- Incremental sync APIs
- Conflict resolution strategies

## Future Enhancements

- Multi-branch support
- Employee management
- Payroll system
- Advanced accounting
- Loyalty program enhancements
- E-commerce integration
- Advanced analytics with AI

## Support

For issues and questions, please open an issue on the repository.

## License

Copyright © 2024. All rights reserved.
