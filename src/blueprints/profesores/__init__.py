from flask import Blueprint

bp = Blueprint('profesores', __name__)

from src.blueprints.profesores import routes