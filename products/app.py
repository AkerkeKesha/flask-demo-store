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


