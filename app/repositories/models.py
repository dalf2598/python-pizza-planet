from datetime import datetime

from app.plugins import db


class Order(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(80))
    client_dni = db.Column(db.String(10))
    client_address = db.Column(db.String(128))
    client_phone = db.Column(db.String(15))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    total_price = db.Column(db.Float)

    detail = db.relationship('OrderDetail', backref=db.backref('order_detail'))


class Ingredient(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Size(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Beverage(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)

class OrderDetail(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order._id'))
    ingredient = db.relationship('Ingredient', backref=db.backref('ingredient'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient._id'))
    ingredient_price = db.Column(db.Float)
    size = db.relationship('Size', backref=db.backref('size'))
    size_id = db.Column(db.Integer, db.ForeignKey('size._id'))
    size_price = db.Column(db.Float)
    beverage = db.relationship('Beverage', backref=db.backref('beverage'))
    beverage_id = db.Column(db.Integer, db.ForeignKey('beverage._id'))
    beverage_price = db.Column(db.Float)
    