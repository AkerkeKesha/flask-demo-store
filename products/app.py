# ============ #
# Products App #
# ============ #
from flask import Blueprint, render_template


products_app = Blueprint("products_app", __name__,
                         template_folder="./templates",
                         static_folder="./static",
                         static_url_path='products/static')


@products_app.route("/", methods=["GET"])
def show_products():
    return "need to render products"


