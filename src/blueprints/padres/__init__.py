from flask import Blueprint

bp = Blueprint('padres', __name__)

from src.blueprints.padres import routes