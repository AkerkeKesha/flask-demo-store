# ============ #
# Products App #
# ============ #
from flask import Blueprint, render_template

from core.database import init_db, db_session
from products.models import Product


products_app = Blueprint("products_app", __name__,
                         template_folder="./templates",
                         static_folder="./static",
                         static_url_path='products/static')
init_db()


@products_app.route("/", methods=["GET"])
def show_products():
    products = Product.query.all()
    template_path = "products/products.html"
    context = {
        "products": products,
        "products_page": True,

    }
    return render_template(template_path, **context)


@products_app.route("/add_products", methods=["GET"])
def add_products():
    db_session.add(Product('Computer', 15, 'Xiaomi Laptop very convenient and easy to use', 'laptop.jpeg'))
    db_session.add(Product('Mobile', 10, 'This model of Samsung Galaxy Note8 is luxurious and trendy this season', 'note8.jpeg'))
    db_session.add(Product('Watch', 5, 'Xiaomi Laptop very convenient and easy to use', 'watch.jpg'))
    db_session.commit()
    return "Items added..."


@products_app.route("/<int:product_id>", methods=["GET", "POST"])
def show_single_product(product_id):
    product = db_session.query(Product).get(product_id)
    if product:
        template_path = "products/product.html"
        context = {
            "product": product,
            "single_product_page": True,
        }
        return render_template(template_path, **context)
    else:
        template_path = "404.html"
        return render_template(template_path), 404


