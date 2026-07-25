"""
Product Schemas
"""
from marshmallow import Schema, fields, validate
from app.schemas.base import BaseSchema
from app.models.product import Product, Category, Brand


class CategorySchema(BaseSchema):
    """Category schema"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    description = fields.Str(allow_none=True)
    
    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


class BrandSchema(BaseSchema):
    """Brand schema"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    description = fields.Str(allow_none=True)
    
    class Meta:
        model = Brand
        fields = ('id', 'name', 'description', 'created_at', 'updated_at')


class ProductSchema(BaseSchema):
    """Product schema"""
    product_code = fields.Str(dump_only=True)
    barcode = fields.Str(dump_only=True)
    qr_code = fields.Str(dump_only=True, allow_none=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str(allow_none=True)
    category_id = fields.Str(required=True)
    brand_id = fields.Str(required=True)
    gender = fields.Str(
        required=True,
        validate=validate.OneOf(['men', 'women', 'kids', 'unisex'])
    )
    color = fields.Str(allow_none=True, validate=validate.Length(max=50))
    size = fields.Str(allow_none=True, validate=validate.Length(max=20))
    buying_price = fields.Decimal(required=True, places=2)
    selling_price = fields.Decimal(required=True, places=2)
    quantity = fields.Integer(dump_only=True)
    minimum_stock = fields.Integer(required=True, validate=validate.Range(min=0))
    supplier_id = fields.Str(allow_none=True)
    image = fields.Str(allow_none=True)
    status = fields.Str(dump_only=True)
    created_by = fields.Str(dump_only=True)
    
    # Nested fields
    category = fields.Nested(CategorySchema, dump_only=True)
    brand = fields.Nested(BrandSchema, dump_only=True)
    
    # Computed fields
    is_low_stock = fields.Boolean(dump_only=True)
    is_out_of_stock = fields.Boolean(dump_only=True)
    profit_margin = fields.Float(dump_only=True)
    
    class Meta:
        model = Product
        fields = (
            'id', 'product_code', 'barcode', 'qr_code', 'name', 'description',
            'category_id', 'brand_id', 'gender', 'color', 'size',
            'buying_price', 'selling_price', 'quantity', 'minimum_stock',
            'supplier_id', 'image', 'status', 'created_by',
            'category', 'brand', 'is_low_stock', 'is_out_of_stock',
            'profit_margin', 'created_at', 'updated_at'
        )


class ProductCreateSchema(Schema):
    """Product creation schema"""
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    description = fields.Str(allow_none=True)
    category_id = fields.Str(required=True)
    brand_id = fields.Str(required=True)
    gender = fields.Str(
        required=True,
        validate=validate.OneOf(['men', 'women', 'kids', 'unisex'])
    )
    color = fields.Str(allow_none=True, validate=validate.Length(max=50))
    size = fields.Str(allow_none=True, validate=validate.Length(max=20))
    buying_price = fields.Decimal(required=True, places=2, validate=validate.Range(min=0))
    selling_price = fields.Decimal(required=True, places=2, validate=validate.Range(min=0))
    minimum_stock = fields.Integer(required=True, validate=validate.Range(min=0))
    supplier_id = fields.Str(allow_none=True)
    image = fields.Str(allow_none=True)


class ProductUpdateSchema(Schema):
    """Product update schema"""
    name = fields.Str(validate=validate.Length(min=1, max=100))
    description = fields.Str(allow_none=True)
    category_id = fields.Str()
    brand_id = fields.Str()
    gender = fields.Str(validate=validate.OneOf(['men', 'women', 'kids', 'unisex']))
    color = fields.Str(allow_none=True, validate=validate.Length(max=50))
    size = fields.Str(allow_none=True, validate=validate.Length(max=20))
    buying_price = fields.Decimal(places=2, validate=validate.Range(min=0))
    selling_price = fields.Decimal(places=2, validate=validate.Range(min=0))
    minimum_stock = fields.Integer(validate=validate.Range(min=0))
    supplier_id = fields.Str(allow_none=True)
    image = fields.Str(allow_none=True)
    status = fields.Str(validate=validate.OneOf(['active', 'inactive', 'discontinued']))
