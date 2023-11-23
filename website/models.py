from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    carts = db.relationship('Cart')

    def __repr__(self):
        return f"User('{self.id}', '{self.email}', '{self.first_name}')\n"

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_producto = db.Column(db.String(500))
    precio_producto = db.Column(db.Float)
    imagen_producto = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Cart('{self.id}', '{self.nombre_producto}', '{self.precio_producto}', '{self.imagen_producto}', '{self.user_id}')"