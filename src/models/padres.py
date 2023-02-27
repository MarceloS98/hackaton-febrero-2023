from src.extentions import db
from src.models.padres_avisos import padres_avisos

class Padres(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_padres = db.Column(db.String(50))
    nro_contacto = db.Column(db.Integer())
    rol_padres = db.Column(db.String(50))

    # conexion entre padres y alumnos
    alumnos_id = db.relationship('Alumnos', backref='padres')

    following = db.relationship('Avisos', secondary=padres_avisos, backref='followers')