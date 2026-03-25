#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Render the items page with data from items.json."""
    with open('items.json', 'r') as file:
        items_data = json.load(file)
    return render_template('items.html', items=items_data["items"])


@app.route('/products')
def products():
    """Render the products page with data from
      either products.json or products.csv based on query parameters."""
    source = request.args.get('source')
    id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        products_data = read_json()
    elif source == 'sql':
        products_data = read_sql()
    else:
        products_data = read_csv()

    if id:
        products_data = [product for product in products_data
                         if product['id'] == int(id)]
        if not products_data:
            return render_template('product_display.html', error="Product not found")
    return render_template('product_display.html', products=products_data)


def read_json():
    """Read products from products.json and
      return as a list of dictionaries."""
    with open('products.json', 'r') as file:
        return json.load(file)


def read_csv():
    """Read products from products.csv and
      return as a list of dictionaries."""
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        return [{"id": int(row["id"]),
                 "name": row["name"],
                 "category": row["category"],
                 "price": float(row["price"])}
                for row in reader]


def read_sql():
    """Read products from products.db and
      return as a list of dictionaries."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": row[0],
             "name": row[1],
             "category": row[2],
             "price": row[3]}
            for row in rows]


if __name__ == "__main__":
    app.run(debug=True, port=5000)
