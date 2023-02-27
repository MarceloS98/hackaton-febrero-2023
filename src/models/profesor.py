from src.extentions import db

class Profesor(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name_profesor = db.Column(db.String(20))
    rol_profesor = db.Column(db.String(20))
    ci_profesor = db.Column(db.Integer())
    seccion_profesor = db.Column(db.String(10))
    grupo = db.Column(db.String(10))

    # conexion entre profesor y alumnos
    alumnos = db.relationship('Alumnos', backref='profesor')
    # conexion entre profesor y avisos
    avisos = db.relationship('Avisos', backref='profesor')
    # conexion entre profesor y materias
    materias = db.relationship('Materias', backref='profesor')