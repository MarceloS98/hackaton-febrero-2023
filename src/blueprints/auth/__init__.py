from flask import Blueprint

bp = Blueprint('auth', __name__)

from src.blueprints.auth import routes