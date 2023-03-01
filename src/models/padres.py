from flask_login import UserMixin
from src.extentions import db

class Padres(UserMixin,db.Model):
    padre_id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    nro_contacto = db.Column(db.Integer())
    rol = db.Column(db.String(50))
    ci = db.Column(db.Integer())
    password = db.Column(db.String(10))

    # conexion entre padres y alumnos
    hijo = db.relationship('Alumnos', backref='padres', uselist=False)

    def get_id(self):
        return str(self.padre_id)
    
