"""
User, Role, and Permission Models
"""
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db
from .base import BaseModel


class Role(BaseModel):
    """Role model for RBAC"""
    __tablename__ = 'roles'
    
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(255))
    
    # Relationships
    users = db.relationship('User', secondary='user_roles', back_populates='roles')
    permissions = db.relationship(
        'Permission',
        secondary='role_permissions',
        back_populates='roles'
    )
    
    def __repr__(self) -> str:
        return f"<Role {self.name}>"


class Permission(BaseModel):
    """Permission model for RBAC"""
    __tablename__ = 'permissions'
    
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255))
    module = db.Column(db.String(50), nullable=False)  # products, sales, etc.
    
    # Relationships
    roles = db.relationship(
        'Role',
        secondary='role_permissions',
        back_populates='permissions'
    )
    
    def __repr__(self) -> str:
        return f"<Permission {self.name}>"


class RolePermission(BaseModel):
    """Many-to-many relationship between roles and permissions"""
    __tablename__ = 'role_permissions'
    
    role_id = db.Column(
        db.String(36),
        db.ForeignKey('roles.id'),
        nullable=False
    )
    permission_id = db.Column(
        db.String(36),
        db.ForeignKey('permissions.id'),
        nullable=False
    )
    
    # Unique constraint
    __table_args__ = (
        db.UniqueConstraint('role_id', 'permission_id', name='unique_role_permission'),
    )


class User(BaseModel):
    """User model"""
    __tablename__ = 'users'
    
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    email = db.Column(db.String(100), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(255))
    profile_image = db.Column(db.String(255))
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    last_login = db.Column(db.DateTime)
    
    # Relationships
    roles = db.relationship('Role', secondary='user_roles', back_populates='users')
    sales = db.relationship('Sale', back_populates='cashier')
    created_products = db.relationship('Product', back_populates='created_by_user')
    
    def set_password(self, password: str) -> None:
        """Hash and set password"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password: str) -> bool:
        """Check if provided password matches hash"""
        return check_password_hash(self.password_hash, password)
    
    def has_permission(self, permission_name: str) -> bool:
        """Check if user has a specific permission"""
        for role in self.roles:
            for permission in role.permissions:
                if permission.name == permission_name:
                    return True
        return False
    
    def has_role(self, role_name: str) -> bool:
        """Check if user has a specific role"""
        return any(role.name == role_name for role in self.roles)
    
    def update_last_login(self) -> None:
        """Update last login timestamp"""
        self.last_login = datetime.utcnow()
    
    def __repr__(self) -> str:
        return f"<User {self.username}>"


# Association table for user-roles
user_roles = db.Table(
    'user_roles',
    db.Column(
        'user_id',
        db.String(36),
        db.ForeignKey('users.id'),
        nullable=False
    ),
    db.Column(
        'role_id',
        db.String(36),
        db.ForeignKey('roles.id'),
        nullable=False
    ),
    db.UniqueConstraint('user_id', 'role_id', name='unique_user_role')
)
