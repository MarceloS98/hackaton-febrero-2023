alumnos_materias = db.Table('alumnos_materias', 
    db.Column('alumnos_id', db.Integer, db.ForeignKey('alumnos.id')), 
    db.Column('materias_id', db.Integer, db.ForeignKey ('materias.id'))
)