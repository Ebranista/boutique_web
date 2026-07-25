from flask import Flask
from app.extensions import db
from app.models.product import Product, Category, Brand
from app.models.supplier import Supplier
from app.models.user import User
from app.services.purchase_service import PurchaseService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db.init_app(app)
    db.create_all()

    supplier = Supplier(name='Test Supplier', phone='1234567890')
    user = User(username='admin', email='admin@example.com', first_name='Admin', last_name='User')
    user.set_password('pass')
    category = Category(name='TestCat')
    brand = Brand(name='TestBrand')
    db.session.add_all([supplier, user, category, brand])
    db.session.commit()

    product = Product(
        product_code='P001',
        name='Test Product',
        category_id=category.id,
        brand_id=brand.id,
        gender='unisex',
        buying_price=10,
        selling_price=20,
        minimum_stock=5,
        created_by=user.id
    )
    db.session.add(product)
    db.session.commit()

    print('Created', supplier.id, user.id, product.id)

    svc = PurchaseService()
    try:
        purchase = svc.create_purchase({
            'supplier_id': supplier.id,
            'payment_method': 'cash',
            'paid_amount': 250.00,
            'notes': 'Test purchase',
            'items': [
                {
                    'product_id': product.id,
                    'quantity': 20,
                    'buying_price': 12.50
                }
            ]
        }, user.id)
        print('Purchase success', purchase.id, purchase.subtotal, purchase.tax, purchase.total, purchase.balance)
    except Exception as exc:
        import traceback
        traceback.print_exc()
