from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Cart
from . import db
import json
import requests
import random

def single_product(productos_id):
    r = requests.get(f'https://fakestoreapi.com/products/{random.choice(productos_id)}')
    r.status_code
    response = r.json()
    return response


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    productos_id = [*range(1,21)]

    producto = single_product(productos_id)

    data = {
        "nombre_producto": producto['title'],
        "precio_producto": f"{producto['price']}",
        "imagen_producto": producto['image']
    }

    if request.method == 'POST':
        nombre_producto = request.form.get('nombre_producto')
        precio_producto = request.form.get('precio_producto')
        imagen_producto = request.form.get('imagen_producto')
        
        print(f"Esto vale nombre_producto: {nombre_producto}")
        print(f"Esto vale precio_producto: {precio_producto}")
        print(f"Esto vale imagen_producto: {imagen_producto}")
        print(f"Esto vale current_user.id: {current_user.id}")

        added_product = Cart(nombre_producto=nombre_producto, precio_producto=precio_producto, imagen_producto=imagen_producto, user_id=current_user.id)
        db.session.add(added_product)
        db.session.commit()
        flash(f'"{nombre_producto}" fue agregado al carrito', category="success")


    return render_template("home.html", user=current_user, data=data)

@views.route('/delete-cart', methods=['POST'])
def delete_card():
    cart = json.loads(request.data)
    cartId = cart['cartId']
    cart = Cart.query.get(cartId)

    if cart:
        if cart.user_id == current_user.id:
            db.session.delete(cart)
            db.session.commit()

        return jsonify({})


@views.route('/cart')
@login_required
def cart():
    return render_template("cart.html", user=current_user)