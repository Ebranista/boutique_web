"""
Authentication Tests
"""
import pytest
from flask import json


def test_login_success(client):
    """Test successful login"""
    # First create a test user
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
    
    # Test login
    response = client.post('/api/v1/auth/login', 
                          data=json.dumps({
                              'username': 'testuser',
                              'password': 'TestPassword123'
                          }),
                          content_type='application/json')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['success'] == True
    assert 'access_token' in data['data']
    assert 'refresh_token' in data['data']


def test_login_invalid_credentials(client):
    """Test login with invalid credentials"""
    response = client.post('/api/v1/auth/login',
                          data=json.dumps({
                              'username': 'wronguser',
                              'password': 'wrongpassword'
                          }),
                          content_type='application/json')
    
    assert response.status_code == 401
    data = json.loads(response.data)
    assert data['success'] == False


def test_login_validation_error(client):
    """Test login with missing fields"""
    response = client.post('/api/v1/auth/login',
                          data=json.dumps({
                              'username': 'testuser'
                          }),
                          content_type='application/json')
    
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['success'] == False
