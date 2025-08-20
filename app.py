from flask import Flask, render_template, jsonify

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 50000, "desc": "High performance laptop"},
    {"id": 2, "name": "Smartphone", "price": 25000, "desc": "Latest 5G smartphone"},
    {"id": 3, "name": "Headphones", "price": 3000, "desc": "Noise cancelling headphones"},
    {"id": 4, "name": "Keyboard", "price": 1200, "desc": "Mechanical keyboard"},
    {"id": 5, "name": "Smartwatch", "price": 7000, "desc": "Fitness smartwatch"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/products")
def get_products():
    return jsonify(PRODUCTS)

if __name__ == "__main__":
    app.run(debug=True)
