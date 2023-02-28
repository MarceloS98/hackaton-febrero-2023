from flask import Flask 
from config import Config
from src.extentions import db, login_manager

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializamos las extensiones de Flask
    db.init_app(app)
    login_manager.init_app(app)

    # Modelos
    from src.models.alumnos import Alumnos
    from src.models.avisos import Avisos
    from src.models.padres import Padres
    from src.models.profesor import Profesor
    from src.models.materias import Materias

    # Blueprints(rutas)
    from src.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from src.blueprints.padres import bp as padres_bp
    app.register_blueprint(padres_bp, url_prefix='/padres')

    from src.blueprints.profesores import bp as profesores_bp
    app.register_blueprint(profesores_bp, url_prefix='/profesores')

    # Login manager
    @login_manager.user_loader
    def load_user(id):
        padre = Padres.query.filter_by(padre_id=id).first()
        profesor = Profesor.query.filter_by(profesor_id=id).first()
        return padre or profesor

    # Cargar datos en la db
    # tamara = Profesor(name='Tamara Cantero', rol= 'profesor', ci=5975992, grupo='5A', password='tammy')
    # diego = Padres(name='Diego Evers', nro_contacto='971777409', rol='padre',  ci=971777409, password='diego')

    # with app.app_context():
    #      db.create_all()
    #      db.session.add_all([tamara, diego])
    #      db.session.commit()

    return app