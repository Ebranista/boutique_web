"""
Product Tests
"""
import pytest
from flask import json


def test_create_product(client):
    """Test product creation"""
    # First create category and brand
    from app.models.product import Category, Brand
    from app.models.user import User, Role
    from app.extensions import db
    
    role = Role(name='Administrator', description='Admin role')
    db.session.add(role)
    db.session.commit()
    
    user = User(
        username='testuser',
        email='test@example.com',
        first_name='Test',
        last_name='User'
    )
    user.set_password('TestPassword123')
    user.roles.append(role)
    db.session.add(user)
    db.session.commit()
    
    category = Category(name='Clothes', description='Clothing items')
    db.session.add(category)
    
    brand = Brand(name='Nike', description='Nike brand')
    db.session.add(brand)
    db.session.commit()
    
    # Login to get token
    response = client.post('/api/v1/auth/login',
                          data=json.dumps({
                              'username': 'testuser',
                              'password': 'TestPassword123'
                          }),
                          content_type='application/json')
    token = json.loads(response.data)['data']['access_token']
    
    # Create product
    response = client.post('/api/v1/products',
                          data=json.dumps({
                              'name': 'Test T-Shirt',
                              'category_id': category.id,
                              'brand_id': brand.id,
                              'gender': 'unisex',
                              'buying_price': 10.00,
                              'selling_price': 25.00,
                              'minimum_stock': 10
                          }),
                          content_type='application/json',
                          headers={'Authorization': f'Bearer {token}'})
    
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['success'] == True
    assert data['data']['name'] == 'Test T-Shirt'


def test_get_products(client):
    """Test getting products list"""
    response = client.get('/api/v1/products')
    assert response.status_code == 401  # Unauthorized without token


def test_product_validation(client):
    """Test product validation"""
    from app.models.user import User, Role
    from app.extensions import db
    
    role = Role(name='Administrator', description='Admin role')
    db.session.add(role)
    db.session.commit()
    
    user = User(
        username='testuser',
        email='test@example.com',
        first_name='Test',
        last_name='User'
    )
    user.set_password('TestPassword123')
    user.roles.append(role)
    db.session.add(user)
    db.session.commit()
    
    response = client.post('/api/v1/auth/login',
                          data=json.dumps({
                              'username': 'testuser',
                              'password': 'TestPassword123'
                          }),
                          content_type='application/json')
    token = json.loads(response.data)['data']['access_token']
    
    # Try to create product without required fields
    response = client.post('/api/v1/products',
                          data=json.dumps({
                              'name': 'Test Product'
                          }),
                          content_type='application/json',
                          headers={'Authorization': f'Bearer {token}'})
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] == False
