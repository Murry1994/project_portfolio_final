from flask import Blueprint, jsonify, request
from my_store import Category, Cart, Customer, Product, Payment, Order, db
import hashlib
import secrets
from my_store import Category, Product, Customer, Order

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([category.name for category in categories])


@bp.route('categories', methods=['POST'])
def add_category():
    category_id = request.get_json()
    name = data.get('name')
    description = data.get('description')

    new_category = Category(name=name, description=description)
    db.session.add(new_category)
    db.session.commit()

    return jsonify({"message": "Category added", "category": name}), 201


@bp.route('products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([
        {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': product.price,
        }
        for product in products
    ])


@bp.route('products', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    
    category = Category.query.get(category.id)
    if not category:
        return jsonify({"message": "Category not found"}), 404

    new_product = Product(
        name=name, 
        description=description, 
        price=price, 
    )

    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product added", "product": name}), 201


@bp.route('customers/<int:user_id>', methods=['GET'])
def get_customer(user_id):
    customer = Customer.query.get_or_404(user_id)
    return jsonify({
        'id': user_id,
        'first_name': customer.first_name,
        'last_name': customer.last_name,
        'email': customer.email,
        'address': customer.address,
        'phone_number': customer.phone_number
    })


@bp.route('customers/<int:customer_id>/orders', methods=['GET'])
def get_orders_for_customer(user_id):
    customer = Customer.query.get_or_404(user_id)
    orders = customer.orders
    return jsonify([
        {
            'id': order.id,
            'order_date': order.order_date,
            'status': order.status
        }
        for order in orders
    ])


@bp.route('orders', methods=['POST'])
def create_order():
    data = request.get_json()
    order_id = data.get('order_id')
    status = data.get('status')

    customer = Customer.query.get(order_id)
    if not customer:
        return jsonify({"message": "Customer not found"}), 404

    new_order = Order(customer_id=order_id, status=status)
    db.session.add(new_order)
    db.session.commit()

    return jsonify({"message": "Order created", "order_id": new_order.id}), 201


