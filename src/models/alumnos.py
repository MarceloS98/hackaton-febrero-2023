from src.extentions import db
from src.models.alumnos_materias import alumnos_materias
from src.models.alumnos_avisos import alumnos_avisos

class Alumnos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_alumno = db.Column(db.String(20))
    ci_alumno = db.Column(db.Integer())
    seccion_alumno = db.Column(db.String(10))
    curso = db.Column(db.String(10))
   
    #conexion de profesor y alumnos
    profesor_id = db.Column(db.Integer, db.ForeignKey('profesor.id'))
    #conexion de padres y alumnos
    padres_id = db.Column(db.Integer, db.ForeignKey('padres.id'))


    # alumnos/materias
    following = db.relationship('Materias', secondary=alumnos_materias, backref='followers')

    # alumnos/avisos
    following = db.relationship('Avisos', secondary=alumnos_avisos, backref='followers')

    def __repr__(self):
        return f'<Alumno: {self.name_alumno, self.ci_alumno, self.seccion_alumno, self.curso}>'
    