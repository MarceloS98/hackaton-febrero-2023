alumnos_avisos = db.Table('alumnos_avisos', 
    db.Column('alumnos_id', db.Integer, db.ForeignKey('alumnos.id')), 
    db.Column('avisos_id', db.Integer, db.ForeignKey ('avisos.id'))
)