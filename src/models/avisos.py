from src.extentions import db

class Avisos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50))
    cuerpo = db.Column(db.String(250))

    #conexion entre avisos  y profesor
    profesor_id = db.Column(db.Integer, db.ForeignKey('profesor.id'))

    def __repr__(self):
        return f'<Avisos: {self.titulo, self.cuerpo}'