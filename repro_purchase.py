from app import create_app
from app.extensions import db
from app.models.supplier import Supplier
from app.models.product import Product, Category, Brand
from app.models.user import User
from app.services.purchase_service import PurchaseService

app = create_app('testing')
with app.app_context():
    db.drop_all()
    db.create_all()

    supplier = Supplier(name='Test Supplier', phone='1234567890')
    user = User(username='admin', password='pass', email='admin@example.com', created_by='')
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

    print('Created entities', supplier.id, user.id, product.id)

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
