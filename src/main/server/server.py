from flask import Flask
from src.main.routes.orders_routes import orders_routes_bp

app = Flask(__name__)
app.register_blueprint(orders_routes_bp)