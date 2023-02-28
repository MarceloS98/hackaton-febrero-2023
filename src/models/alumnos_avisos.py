from src.extentions import db

alumnos_avisos = db.Table('alumnos_avisos', 
    db.Column('alumnos_id', db.Integer, db.ForeignKey('alumnos.alumnos_id')), 
    db.Column('avisos_id', db.Integer, db.ForeignKey ('avisos.id'))
)