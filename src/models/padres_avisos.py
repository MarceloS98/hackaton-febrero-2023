from src.extentions import db

padres_avisos = db.Table('padres_avisos', 
    db.Column('padres_id', db.Integer, db.ForeignKey('padres.padre_id')), 
    db.Column('avisos_id', db.Integer, db.ForeignKey('avisos.id'))
)