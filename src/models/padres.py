from flask_login import UserMixin
from src.extentions import db
from src.models.padres_avisos import padres_avisos

class Padres(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    nro_contacto = db.Column(db.Integer())
    rol = db.Column(db.String(50))
    ci = db.Column(db.Integer())
    password = db.Column(db.String(10))

    # conexion entre padres y alumnos
    alumnos_id = db.relationship('Alumnos', backref='padres')

    avisos = db.relationship('Avisos', secondary=padres_avisos, backref='padres')