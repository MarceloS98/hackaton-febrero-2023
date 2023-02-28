import uuid
from flask_login import UserMixin
from src.extentions import db
from src.models.padres_avisos import padres_avisos

class Padres(UserMixin,db.Model):
    padre_id = db.Column(db.String(32), primary_key = True, default=str(uuid.uuid4()))
    name = db.Column(db.String(50))
    nro_contacto = db.Column(db.Integer())
    rol = db.Column(db.String(50))
    ci = db.Column(db.Integer())
    password = db.Column(db.String(10))

    # conexion entre padres y alumnos
    alumnos_id = db.relationship('Alumnos', backref='padres')

    avisos = db.relationship('Avisos', secondary=padres_avisos, backref='padres')

    def get_id(self):
        return str(self.padre_id)
    
