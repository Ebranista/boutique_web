# Boutique Shop Management API Documentation

**Base URL:** `http://localhost:5000/api/v1`

**Authentication:** JWT Bearer Token (include in Authorization header: `Bearer <token>`)

---

## Table of Contents
1. [Authentication](#authentication)
2. [Categories](#categories)
3. [Brands](#brands)
4. [Products](#products)
5. [Inventory](#inventory)
6. [Suppliers](#suppliers)
7. [Customers](#customers)
8. [Purchases](#purchases)
9. [Sales](#sales)
10. [Expenses](#expenses)
11. [Users](#users)
12. [Dashboard](#dashboard)
13. [Reports](#reports)
14. [Notifications](#notifications)
15. [Settings](#settings)
16. [Audit Logs](#audit-logs)

---

## Authentication

### Login
**Endpoint:** `POST /auth/login`

**Request Body:**
```json
{
  "username": "admin",
  "password": "Admin123!"
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "Login successful",
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "user": {
      "id": "uuid",
      "username": "admin",
      "email": "admin@boutique.com",
      "first_name": "System",
      "last_name": "Administrator"
    }
  }
}
```

### Refresh Token
**Endpoint:** `POST /auth/refresh`

**Request Body:**
```json
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "Token refreshed",
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
  }
}
```

### Logout
**Endpoint:** `POST /auth/logout`
**Auth Required:** Yes

**Response (200):**
```json
{
  "success": true,
  "message": "Logout successful"
}
```

### Change Password
**Endpoint:** `POST /auth/change-password`
**Auth Required:** Yes

**Request Body:**
```json
{
  "old_password": "OldPass123!",
  "new_password": "NewPass123!"
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "Password changed successfully"
}
```

### Get Current User
**Endpoint:** `GET /auth/me`
**Auth Required:** Yes

**Response (200):**
```json
{
  "success": true,
  "message": "User retrieved",
  "data": {
    "id": "uuid",
    "username": "admin",
    "email": "admin@boutique.com",
    "first_name": "System",
    "last_name": "Administrator",
    "phone": "+1234567890",
    "address": null,
    "profile_image": null,
    "is_active": true,
    "last_login": "2026-07-09T13:27:13",
    "roles": [...]
  }
}
```

---

## Categories

### Get All Categories
**Endpoint:** `GET /categories/`
**Auth Required:** Yes
**Query Params:** `page` (default: 1), `per_page` (default: 20)

**Response (200):**
```json
{
  "success": true,
  "message": "Success",
  "data": {
    "items": [
      {
        "id": "uuid",
        "name": "T-Shirts",
        "description": "Premium Cotton T-Shirts",
        "created_at": "2026-07-09T08:27:24",
        "updated_at": "2026-07-09T08:27:24"
      }
    ],
    "pagination": {
      "total": 10,
      "page": 1,
      "per_page": 20,
      "total_pages": 1,
      "has_next": false,
      "has_prev": false
    }
  }
}
```

### Create Category
**Endpoint:** `POST /categories/`
**Auth Required:** Yes (Permission: manage_products)

**Request Body:**
```json
{
  "name": "T-Shirts",
  "description": "Premium Cotton T-Shirts"
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "Category created successfully",
  "data": {
    "id": "uuid",
    "name": "T-Shirts",
    "description": "Premium Cotton T-Shirts",
    "created_at": "2026-07-09T08:27:24",
    "updated_at": "2026-07-09T08:27:24"
  }
}
```

### Get Category by ID
**Endpoint:** `GET /categories/{category_id}`
**Auth Required:** Yes

**Response (200):**
```json
{
  "success": true,
  "message": "Category retrieved",
  "data": {
    "id": "uuid",
    "name": "T-Shirts",
    "description": "Premium Cotton T-Shirts"
  }
}
```

### Update Category
**Endpoint:** `PUT /categories/{category_id}`
**Auth Required:** Yes (Permission: manage_products)

**Request Body:**
```json
{
  "name": "T-Shirts (Updated)",
  "description": "Premium Cotton T-Shirts - Updated Description"
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "Category updated successfully",
  "data": {...}
}
```

### Delete Category
**Endpoint:** `DELETE /categories/{category_id}`
**Auth Required:** Yes (Permission: manage_products)

**Response (200):**
```json
{
  "success": true,
  "message": "Category deleted successfully"
}
```

---

## Brands

### Get All Brands
**Endpoint:** `GET /brands/`
**Auth Required:** Yes
**Query Params:** `page` (default: 1), `per_page` (default: 20)

**Response (200):**
```json
{
  "success": true,
  "message": "Success",
  "data": {
    "items": [
      {
        "id": "uuid",
        "name": "Nike",
        "description": "Nike Activewear",
        "created_at": "2026-07-09T08:27:24",
        "updated_at": "2026-07-09T08:27:24"
      }
    ],
    "pagination": {...}
  }
}
```

### Create Brand
**Endpoint:** `POST /brands/`
**Auth Required:** Yes (Permission: manage_products)

**Request Body:**
```json
{
  "name": "Nike",
  "description": "Nike Activewear"
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "Brand created successfully",
  "data": {...}
}
```

### Get Brand by ID
**Endpoint:** `GET /brands/{brand_id}`
**Auth Required:** Yes

### Update Brand
**Endpoint:** `PUT /brands/{brand_id}`
**Auth Required:** Yes (Permission: manage_products)

### Delete Brand
**Endpoint:** `DELETE /brands/{brand_id}`
**Auth Required:** Yes (Permission: manage_products)

---

## Products

### Get All Products
**Endpoint:** `GET /products/`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`, `category_id`, `brand_id`, `gender`

**Response (200):**
```json
{
  "success": true,
  "message": "Success",
  "data": {
    "items": [
      {
        "id": "uuid",
        "product_code": "PRD-3Q644S9I",
        "barcode": "PRD-3Q644S9I",
        "name": "Nike Dry-Fit Tee",
        "description": "Athletic dry-fit sports t-shirt",
        "category_id": "uuid",
        "brand_id": "uuid",
        "gender": "unisex",
        "color": "Black",
        "size": "L",
        "buying_price": 12.5,
        "selling_price": 35.0,
        "quantity": 100,
        "minimum_stock": 5,
        "supplier_id": null,
        "image": null,
        "status": "active",
        "created_by": "uuid",
        "created_at": "2026-07-09T08:27:24",
        "updated_at": "2026-07-09T08:27:24"
      }
    ],
    "pagination": {...}
  }
}
```

### Create Product
**Endpoint:** `POST /products/`
**Auth Required:** Yes (Permission: manage_products)

**Request Body:**
```json
{
  "name": "Nike Dry-Fit Tee",
  "description": "Athletic dry-fit sports t-shirt",
  "category_id": "uuid",
  "brand_id": "uuid",
  "gender": "unisex",
  "color": "Black",
  "size": "L",
  "buying_price": 12.50,
  "selling_price": 35.00,
  "minimum_stock": 5,
  "supplier_id": "uuid",
  "image": "https://example.com/image.jpg"
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "Product created successfully",
  "data": {...}
}
```

### Get Product by ID
**Endpoint:** `GET /products/{product_id}`
**Auth Required:** Yes

### Update Product
**Endpoint:** `PUT /products/{product_id}`
**Auth Required:** Yes (Permission: manage_products)

**Request Body:**
```json
{
  "name": "Nike Dry-Fit Tee (Updated)",
  "description": "Athletic dry-fit sports t-shirt - Updated",
  "selling_price": 40.00,
  "status": "active"
}
```

### Delete Product
**Endpoint:** `DELETE /products/{product_id}`
**Auth Required:** Yes (Permission: manage_products)

### Search Products
**Endpoint:** `GET /products/search`
**Auth Required:** Yes
**Query Params:** `q` (search term), `page`, `per_page`

### Get Product by Barcode
**Endpoint:** `GET /products/barcode/{barcode}`
**Auth Required:** Yes

### Get Low Stock Products
**Endpoint:** `GET /products/low-stock`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

### Get Out of Stock Products
**Endpoint:** `GET /products/out-of-stock`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

---

## Inventory

### Get All Inventory
**Endpoint:** `GET /inventory/`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

**Response (200):**
```json
{
  "success": true,
  "message": "Success",
  "data": {
    "items": [
      {
        "id": "uuid",
        "product_id": "uuid",
        "product_name": "Nike Dry-Fit Tee",
        "product_code": "PRD-3Q644S9I",
        "quantity": 100,
        "reserved_quantity": 0,
        "available_quantity": 100,
        "average_cost": 12.5,
        "total_value": 1250.0
      }
    ],
    "pagination": {...}
  }
}
```

### Get Inventory by Product
**Endpoint:** `GET /inventory/product/{product_id}`
**Auth Required:** Yes

### Adjust Stock
**Endpoint:** `POST /inventory/adjust`
**Auth Required:** Yes (Permission: manage_inventory)

**Request Body:**
```json
{
  "product_id": "uuid",
  "quantity": 50,
  "adjustment_type": "add",
  "reason": "Stock intake",
  "notes": "Testing automated script addition"
}
```

**adjustment_type values:** `add`, `remove`, `set`

**Response (200):**
```json
{
  "success": true,
  "message": "Stock adjusted successfully",
  "data": {...}
}
```

### Get Low Stock Inventory
**Endpoint:** `GET /inventory/low-stock`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

### Get Out of Stock Inventory
**Endpoint:** `GET /inventory/out-of-stock`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

---

## Suppliers

### Get All Suppliers
**Endpoint:** `GET /suppliers/`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

**Response (200):**
```json
{
  "success": true,
  "message": "Success",
  "data": {
    "items": [
      {
        "id": "uuid",
        "name": "ABC Suppliers Ltd",
        "contact_person": "John Doe",
        "phone": "+251911234567",
        "email": "john@abcsuppliers.com",
        "address": "Addis Ababa, Ethiopia",
        "tin_number": "1234567890",
        "outstanding_balance": 45.0,
        "is_active": true,
        "created_at": "2026-07-09T08:27:24",
        "updated_at": "2026-07-09T08:27:24"
      }
    ],
    "pagination": {...}
  }
}
```

### Create Supplier
**Endpoint:** `POST /suppliers/`
**Auth Required:** Yes (Permission: manage_suppliers)

**Request Body:**
```json
{
  "name": "ABC Suppliers Ltd",
  "contact_person": "John Doe",
  "phone": "+251911234567",
  "email": "john@abcsuppliers.com",
  "address": "Addis Ababa, Ethiopia",
  "tin_number": "1234567890"
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "Supplier created successfully",
  "data": {...}
}
```

### Get Supplier by ID
**Endpoint:** `GET /suppliers/{supplier_id}`
**Auth Required:** Yes

### Update Supplier
**Endpoint:** `PUT /suppliers/{supplier_id}`
**Auth Required:** Yes (Permission: manage_suppliers)

### Delete Supplier
**Endpoint:** `DELETE /suppliers/{supplier_id}`
**Auth Required:** Yes (Permission: manage_suppliers)

### Search Suppliers
**Endpoint:** `GET /suppliers/search`
**Auth Required:** Yes
**Query Params:** `q`, `page`, `per_page`

---

## Customers

### Get All Customers
**Endpoint:** `GET /customers/`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

**Response (200):**
```json
{
  "success": true,
  "message": "Success",
  "data": {
    "items": [
      {
        "id": "uuid",
        "name": "Jane Smith",
        "phone": "+251911987654",
        "email": "jane@example.com",
        "address": "Addis Ababa, Ethiopia",
        "gender": null,
        "birthday": null,
        "image": null,
        "loyalty_points": 0,
        "is_active": true,
        "created_at": "2026-07-09T08:27:24",
        "updated_at": "2026-07-09T08:27:24"
      }
    ],
    "pagination": {...}
  }
}
```

### Create Customer
**Endpoint:** `POST /customers/`
**Auth Required:** Yes (Permission: manage_customers)

**Request Body:**
```json
{
  "name": "Jane Smith",
  "phone": "+251911987654",
  "email": "jane@example.com",
  "address": "Addis Ababa, Ethiopia",
  "gender": "female",
  "birthday": "1990-01-01",
  "image": "https://example.com/image.jpg"
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "Customer created successfully",
  "data": {...}
}
```

### Get Customer by ID
**Endpoint:** `GET /customers/{customer_id}`
**Auth Required:** Yes

### Update Customer
**Endpoint:** `PUT /customers/{customer_id}`
**Auth Required:** Yes (Permission: manage_customers)

### Delete Customer
**Endpoint:** `DELETE /customers/{customer_id}`
**Auth Required:** Yes (Permission: manage_customers)

### Search Customers
**Endpoint:** `GET /customers/search`
**Auth Required:** Yes
**Query Params:** `q`, `page`, `per_page`

### Get Customer by Phone
**Endpoint:** `GET /customers/phone/{phone}`
**Auth Required:** Yes

---

## Purchases

### Get All Purchases
**Endpoint:** `GET /purchases/`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

**Response (200):**
```json
{
  "success": true,
  "message": "Success",
  "data": {
    "items": [
      {
        "id": "uuid",
        "purchase_number": "PUR-20260709-7818",
        "supplier_id": "uuid",
        "subtotal": 250.0,
        "discount": 0.0,
        "tax": 45.0,
        "total": 295.0,
        "payment_method": "cash",
        "paid_amount": 250.0,
        "balance": 45.0,
        "purchase_date": "2026-07-09T13:28:03",
        "status": "pending",
        "notes": "Test purchase",
        "receipt_image": null,
        "created_by": "uuid",
        "created_at": "2026-07-09T13:28:03",
        "updated_at": "2026-07-09T13:28:03"
      }
    ],
    "pagination": {...}
  }
}
```

### Create Purchase
**Endpoint:** `POST /purchases/`
**Auth Required:** Yes (Permission: manage_purchases)

**Request Body:**
```json
{
  "supplier_id": "uuid",
  "discount": 0.0,
  "payment_method": "cash",
  "paid_amount": 250.0,
  "notes": "Test purchase",
  "receipt_image": "https://example.com/receipt.jpg",
  "items": [
    {
      "product_id": "uuid",
      "quantity": 20,
      "unit_cost": 12.50,
      "subtotal": 250.0
    }
  ]
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "Purchase created successfully",
  "data": {...}
}
```

### Get Purchase by ID
**Endpoint:** `GET /purchases/{purchase_id}`
**Auth Required:** Yes

### Complete Purchase
**Endpoint:** `POST /purchases/{purchase_id}/complete`
**Auth Required:** Yes (Permission: manage_purchases)

### Cancel Purchase
**Endpoint:** `POST /purchases/{purchase_id}/cancel`
**Auth Required:** Yes (Permission: manage_purchases)

### Get Purchases by Supplier
**Endpoint:** `GET /purchases/supplier/{supplier_id}`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

---

## Sales

### Get All Sales
**Endpoint:** `GET /sales/`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

**Response (200):**
```json
{
  "success": true,
  "message": "Success",
  "data": {
    "items": [
      {
        "id": "uuid",
        "sale_number": "SAL-20260709-1234",
        "customer_id": "uuid",
        "subtotal": 100.0,
        "discount": 0.0,
        "tax": 18.0,
        "total": 118.0,
        "payment_method": "cash",
        "cash_received": 120.0,
        "change_amount": 2.0,
        "sale_date": "2026-07-09T13:30:00",
        "status": "completed",
        "notes": "Test sale",
        "created_by": "uuid",
        "created_at": "2026-07-09T13:30:00",
        "updated_at": "2026-07-09T13:30:00"
      }
    ],
    "pagination": {...}
  }
}
```

### Create Sale (POS)
**Endpoint:** `POST /sales/`
**Auth Required:** Yes (Permission: manage_sales)

**Request Body:**
```json
{
  "customer_id": "uuid",
  "discount": 0.0,
  "payment_method": "cash",
  "cash_received": 120.0,
  "notes": "Test sale",
  "items": [
    {
      "product_id": "uuid",
      "quantity": 2,
      "unit_price": 50.0,
      "subtotal": 100.0,
      "cost": 25.0,
      "profit": 25.0
    }
  ]
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "Sale created successfully",
  "data": {...}
}
```

### Get Sale by ID
**Endpoint:** `GET /sales/{sale_id}`
**Auth Required:** Yes

### Refund Sale
**Endpoint:** `POST /sales/{sale_id}/refund`
**Auth Required:** Yes (Permission: manage_sales)

### Cancel Sale
**Endpoint:** `POST /sales/{sale_id}/cancel`
**Auth Required:** Yes (Permission: manage_sales)

### Get Today's Sales
**Endpoint:** `GET /sales/today`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

### Get Sales by Customer
**Endpoint:** `GET /sales/customer/{customer_id}`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

---

## Expenses

### Get All Expenses
**Endpoint:** `GET /expenses/`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

**Response (200):**
```json
{
  "success": true,
  "message": "Success",
  "data": {
    "items": [
      {
        "id": "uuid",
        "name": "Electricity bill",
        "description": "Electricity bill",
        "category_id": "uuid",
        "amount": 150.0,
        "expense_date": "2026-07-09T00:00:00",
        "is_recurring": false,
        "recurring_month": null,
        "receipt_image": null,
        "notes": null,
        "created_by": "uuid",
        "created_at": "2026-07-09T13:30:00",
        "updated_at": "2026-07-09T13:30:00"
      }
    ],
    "pagination": {...}
  }
}
```

### Create Expense
**Endpoint:** `POST /expenses/`
**Auth Required:** Yes (Permission: manage_expenses)

**Request Body:**
```json
{
  "name": "Electricity bill",
  "category_id": "uuid",
  "description": "Electricity bill",
  "amount": 150.0,
  "expense_date": "2026-07-09",
  "is_recurring": false,
  "recurring_month": null,
  "receipt_image": "https://example.com/receipt.jpg",
  "notes": "Monthly electricity bill"
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "Expense created successfully",
  "data": {...}
}
```

### Get Expense by ID
**Endpoint:** `GET /expenses/{expense_id}`
**Auth Required:** Yes

### Update Expense
**Endpoint:** `PUT /expenses/{expense_id}`
**Auth Required:** Yes (Permission: manage_expenses)

### Delete Expense
**Endpoint:** `DELETE /expenses/{expense_id}`
**Auth Required:** Yes (Permission: manage_expenses)

### Expense Categories

#### Get All Expense Categories
**Endpoint:** `GET /expenses/categories`
**Auth Required:** Yes

#### Create Expense Category
**Endpoint:** `POST /expenses/categories`
**Auth Required:** Yes (Permission: manage_expenses)

**Request Body:**
```json
{
  "name": "Utilities",
  "description": "Utility bills",
  "is_recurring": false
}
```

#### Get Expense Category by ID
**Endpoint:** `GET /expenses/categories/{category_id}`
**Auth Required:** Yes

#### Update Expense Category
**Endpoint:** `PUT /expenses/categories/{category_id}`
**Auth Required:** Yes (Permission: manage_expenses)

#### Delete Expense Category
**Endpoint:** `DELETE /expenses/categories/{category_id}`
**Auth Required:** Yes (Permission: manage_expenses)

---

## Users

### Get All Users
**Endpoint:** `GET /users/`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

**Response (200):**
```json
{
  "success": true,
  "message": "Success",
  "data": {
    "items": [
      {
        "id": "uuid",
        "username": "admin",
        "email": "admin@boutique.com",
        "first_name": "System",
        "last_name": "Administrator",
        "phone": "+1234567890",
        "address": null,
        "profile_image": null,
        "is_active": true,
        "last_login": "2026-07-09T13:27:13",
        "roles": [...]
      }
    ],
    "pagination": {...}
  }
}
```

### Create User
**Endpoint:** `POST /users/`
**Auth Required:** Yes (Admin only)

**Request Body:**
```json
{
  "username": "testuser",
  "email": "testuser@example.com",
  "password": "Test123!",
  "first_name": "Test",
  "last_name": "User",
  "phone": "+251911111111",
  "address": "Addis Ababa, Ethiopia",
  "role_ids": ["2"]
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "User created successfully",
  "data": {...}
}
```

### Get User by ID
**Endpoint:** `GET /users/{user_id}`
**Auth Required:** Yes

### Update User
**Endpoint:** `PUT /users/{user_id}`
**Auth Required:** Yes (Admin only)

### Delete User
**Endpoint:** `DELETE /users/{user_id}`
**Auth Required:** Yes (Admin only)

---

## Dashboard

### Get Dashboard Summary
**Endpoint:** `GET /dashboard/summary`
**Auth Required:** Yes

**Response (200):**
```json
{
  "success": true,
  "message": "Dashboard summary retrieved",
  "data": {
    "total_sales": 15000.0,
    "total_purchases": 8000.0,
    "total_expenses": 2000.0,
    "total_products": 150,
    "total_customers": 50,
    "total_suppliers": 20,
    "low_stock_products": 5,
    "out_of_stock_products": 2,
    "today_sales": 500.0,
    "today_purchases": 0.0,
    "month_sales": 5000.0,
    "month_purchases": 2000.0
  }
}
```

### Get Today's Stats
**Endpoint:** `GET /dashboard/today-stats`
**Auth Required:** Yes

### Get Monthly Stats
**Endpoint:** `GET /dashboard/monthly-stats`
**Auth Required:** Yes

### Get Inventory Stats
**Endpoint:** `GET /dashboard/inventory-stats`
**Auth Required:** Yes

### Get Entity Counts
**Endpoint:** `GET /dashboard/entity-counts`
**Auth Required:** Yes

### Get Current Capital
**Endpoint:** `GET /dashboard/capital`
**Auth Required:** Yes

### Get Top Selling Products
**Endpoint:** `GET /dashboard/top-products`
**Auth Required:** Yes
**Query Params:** `limit` (default: 10)

### Get Recent Sales
**Endpoint:** `GET /dashboard/recent-sales`
**Auth Required:** Yes
**Query Params:** `limit` (default: 10)

### Get Recent Expenses
**Endpoint:** `GET /dashboard/recent-expenses`
**Auth Required:** Yes
**Query Params:** `limit` (default: 10)

### Get Monthly Chart Data
**Endpoint:** `GET /dashboard/monthly-chart`
**Auth Required:** Yes
**Query Params:** `months` (default: 12)

---

## Reports

### Get Sales Report
**Endpoint:** `GET /reports/sales`
**Auth Required:** Yes
**Query Params:** `start_date`, `end_date`, `page`, `per_page`

**Response (200):**
```json
{
  "success": true,
  "message": "Sales report retrieved",
  "data": {
    "sales": [...],
    "total_sales": 15000.0,
    "total_profit": 5000.0,
    "total_items": 100,
    "total_count": 50,
    "page": 1,
    "per_page": 20
  }
}
```

### Get Purchase Report
**Endpoint:** `GET /reports/purchases`
**Auth Required:** Yes
**Query Params:** `start_date`, `end_date`, `page`, `per_page`

### Get Expense Report
**Endpoint:** `GET /reports/expenses`
**Auth Required:** Yes
**Query Params:** `start_date`, `end_date`, `page`, `per_page`

### Get Inventory Report
**Endpoint:** `GET /reports/inventory`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

### Get Profit Report
**Endpoint:** `GET /reports/profit`
**Auth Required:** Yes
**Query Params:** `start_date`, `end_date`

### Get Product Profit Report
**Endpoint:** `GET /reports/product-profit`
**Auth Required:** Yes
**Query Params:** `start_date`, `end_date`, `limit` (default: 20)

### Get Customer Report
**Endpoint:** `GET /reports/customers`
**Auth Required:** Yes
**Query Params:** `start_date`, `end_date`, `limit` (default: 20)

### Get Supplier Report
**Endpoint:** `GET /reports/suppliers`
**Auth Required:** Yes
**Query Params:** `start_date`, `end_date`, `limit` (default: 20)

---

## Notifications

### Get User Notifications
**Endpoint:** `GET /notifications/`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

**Response (200):**
```json
{
  "success": true,
  "message": "Success",
  "data": {
    "items": [
      {
        "id": "uuid",
        "user_id": "uuid",
        "title": "Low Stock Alert",
        "message": "Product 'Nike Dry-Fit Tee' is running low on stock",
        "type": "warning",
        "is_read": false,
        "created_at": "2026-07-09T13:30:00"
      }
    ],
    "pagination": {...}
  }
}
```

### Get Unread Notifications
**Endpoint:** `GET /notifications/unread`
**Auth Required:** Yes
**Query Params:** `page`, `per_page`

### Mark Notification as Read
**Endpoint:** `POST /notifications/{notification_id}/read`
**Auth Required:** Yes

### Mark All Notifications as Read
**Endpoint:** `POST /notifications/read-all`
**Auth Required:** Yes

---

## Settings

### Get Settings
**Endpoint:** `GET /settings/`
**Auth Required:** Yes

**Response (200):**
```json
{
  "success": true,
  "message": "Settings retrieved",
  "data": {
    "id": "uuid",
    "shop_name": "My Boutique Shop",
    "logo": null,
    "address": null,
    "phone": null,
    "email": null,
    "currency": "USD",
    "currency_symbol": "$",
    "tax_percentage": 18,
    "receipt_footer": "Thank you for shopping with us!",
    "receipt_header": "My Boutique Shop",
    "low_stock_limit": 10,
    "dark_mode": false,
    "tin_number": null,
    "created_at": "2026-07-09T08:17:27",
    "updated_at": "2026-07-09T08:17:27"
  }
}
```

### Update Settings
**Endpoint:** `PUT /settings/`
**Auth Required:** Yes (Admin only)

**Request Body:**
```json
{
  "shop_name": "My Boutique Shop",
  "logo": "https://example.com/logo.png",
  "address": "Addis Ababa, Ethiopia",
  "phone": "+251911123456",
  "email": "info@boutique.com",
  "currency": "ETB",
  "currency_symbol": "Birr",
  "tax_percentage": 18,
  "receipt_footer": "Thank you for shopping with us!",
  "receipt_header": "My Boutique Shop",
  "low_stock_limit": 10,
  "dark_mode": false,
  "tin_number": "1234567890"
}
```

### Initialize Default Settings
**Endpoint:** `POST /settings/initialize`
**Auth Required:** Yes (Admin only)

---

## Audit Logs

### Get All Audit Logs
**Endpoint:** `GET /audit/`
**Auth Required:** Yes (Admin only)
**Query Params:** `page`, `per_page`

**Response (200):**
```json
{
  "success": true,
  "message": "Success",
  "data": {
    "items": [
      {
        "id": "uuid",
        "user_id": "uuid",
        "action": "create",
        "entity_type": "Product",
        "entity_id": "uuid",
        "changes": {...},
        "ip_address": "127.0.0.1",
        "user_agent": "Mozilla/5.0...",
        "created_at": "2026-07-09T13:30:00"
      }
    ],
    "pagination": {...}
  }
}
```

### Get Audit Logs by User
**Endpoint:** `GET /audit/user/{user_id}`
**Auth Required:** Yes (Admin only)
**Query Params:** `page`, `per_page`

### Get Audit Logs by Action
**Endpoint:** `GET /audit/action/{action}`
**Auth Required:** Yes (Admin only)
**Query Params:** `page`, `per_page`

### Get Audit Logs by Entity
**Endpoint:** `GET /audit/entity/{entity_type}/{entity_id}`
**Auth Required:** Yes (Admin only)
**Query Params:** `page`, `per_page`

---

## Common Response Format

### Success Response
```json
{
  "success": true,
  "message": "Operation successful",
  "data": {...}
}
```

### Error Response
```json
{
  "success": false,
  "message": "Error message",
  "errors": {...}
}
```

### Paginated Response
```json
{
  "success": true,
  "message": "Success",
  "data": {
    "items": [...],
    "pagination": {
      "total": 100,
      "page": 1,
      "per_page": 20,
      "total_pages": 5,
      "has_next": true,
      "has_prev": false
    }
  }
}
```

---

## HTTP Status Codes

- **200 OK** - Request successful
- **201 Created** - Resource created successfully
- **400 Bad Request** - Validation error or invalid request
- **401 Unauthorized** - Authentication required or invalid token
- **403 Forbidden** - Insufficient permissions
- **404 Not Found** - Resource not found
- **500 Internal Server Error** - Server error

---

## Notes

1. All datetime fields are in ISO 8601 format
2. All monetary values are returned as floats
3. All IDs are UUID strings
4. Include JWT token in Authorization header: `Bearer <token>`
5. Pagination starts from page 1
6. Default per_page is 20 for most endpoints
