import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey 
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    cart = relationship('Cart', back_populates='customer')
    orders = relationship('Order', back_populates='customer')

    def __init__(self):
        return f"<Customer(id={self.user_id}, name={self.first_name} {self.last_name}, email={self.email})>"


class Order(db.Model):
    __tablename__ = 'orders'
    order_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    payments = relationship('Payment', back_populates='order')
    customers = relationship('Customer', back_populates='orders')

    def __init__(self):
        return f"<Order(id={self.order_id}, amount={self.amount} date={self.date}, username={self.password} password={self.password})>"


class Payment(db.Model):
    __tablename__ = 'payments'
    payment_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String, nullable=False)
    amount = db.Column(db.Date, nullable=False)
   
    orders = relationship('Order', back_populates='payment')

    def __init__(self):
        return f"<Payment(id={self.user_idpayment.id}, type={self.type} amount{self.amount})>"




class Product(db.Model):
    __tablename__ = 'products'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, unique=True, nullable=True)

    category = relationship('Category', back_populates='products')

    def __init__(self):
        return f"<Product(id={self.product_id}, name={self.name} price={self.price}, description={self.description})>"



class Category(db.Model):
    __tablename__ = 'categories'
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    

    products = relationship('Product', back_populates='category')

    def __init__(self):
        return f"<Category(id={self.category_id}, name={self.name} description={self.description})>"



class Cart(db.Model):
    __tablename__ = 'cart'
    cart_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('customer_id'))
    description = db.Column(db.String, nullable=True)
    
    products = relationship('Product', back_populates='category')
    customers = relationship('Customer', back_populates='cart')

    def __init__(self):
        return f"<Cart(id={self.cart_id}, user_id={self.user_id} description={self.description})>"
    



