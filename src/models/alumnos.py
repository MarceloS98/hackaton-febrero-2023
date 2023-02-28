from src.extentions import db
from src.models.alumnos_materias import alumnos_materias
from src.models.alumnos_avisos import alumnos_avisos

class Alumnos(db.Model):
    alumnos_id = db.Column(db.Integer, primary_key=True)
    name_alumno = db.Column(db.String(20))
    ci_alumno = db.Column(db.Integer())
    grupo = db.Column(db.String(10))
   
    #conexion de profesor y alumnos
    profesor_id = db.Column(db.Integer, db.ForeignKey('profesor.profesor_id'))
    #conexion de padres y alumnos
    padres_id = db.Column(db.Integer, db.ForeignKey('padres.padre_id'))


    # alumnos/materias
    materias = db.relationship('Materias', secondary=alumnos_materias, backref='followers')

    # alumnos/avisos
    avisos = db.relationship('Avisos', secondary=alumnos_avisos, backref='followers')

    def __repr__(self):
        return f'<Alumno: {self.name_alumno, self.ci_alumno, self.grupo}>'
    