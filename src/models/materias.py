from src.extentions import db

class Materias(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_materia = db.Column(db.String(20))
    etapa_1 = db.Column(db.Integer())
    etapa_2 = db.Column(db.Integer())
    promedio_final = db.Column(db.Integer())

    #conexion entre materias y profesor
    profesor_id = db.Column(db.Integer, db.ForeignKey('profesor.profesor_id'))

    def __repr__(self):
        return f'<Materias: {self.name_materia, self.etapa_1, self.etapa_2, self.promedio_final}'
