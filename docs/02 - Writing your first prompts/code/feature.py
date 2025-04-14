from flask import Flask, jsonify, request

products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.0},
    {'id': 2, 'name': 'Product 2', 'price': 20.0},
    {'id': 3, 'name': 'Product 3', 'price': 30.0},
    {'id': 4, 'name': 'Product 4', 'price': 40.0},
    {'id': 5, 'name': 'Product 5', 'price': 50.0},
    {'id': 6, 'name': 'Product 6', 'price': 60.0},
    {'id': 7, 'name': 'Product 7', 'price': 70.0},
    {'id': 8, 'name': 'Product 8', 'price': 80.0},
    {'id': 9, 'name': 'Product 9', 'price': 90.0},
    {'id': 10, 'name': 'Product 10', 'price': 100.0}
]

## add routes
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    return jsonify(product) if product else ('', 404)

## create a Flask app
app = Flask(__name__)