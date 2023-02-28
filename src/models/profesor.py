import uuid
from flask_login import UserMixin
from src.extentions import db

class Profesor(UserMixin,db.Model):
    profesor_id = db.Column(db.String(32), primary_key = True, default=str(uuid.uuid4()))
    name = db.Column(db.String(20))
    rol = db.Column(db.String(20))
    ci = db.Column(db.Integer())
    grupo = db.Column(db.String(10))
    password = db.Column(db.String(10))

    # conexion entre profesor y alumnos
    alumnos = db.relationship('Alumnos', backref='profesor')
    # conexion entre profesor y avisos
    avisos = db.relationship('Avisos', backref='profesor')
    # conexion entre profesor y materias
    materias = db.relationship('Materias', backref='profesor')

    def get_id(self):
        return str(self.profesor_id)


