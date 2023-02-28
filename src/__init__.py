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
    app.register_blueprint(padres_bp)

    from src.blueprints.profesores import bp as profesores_bp
    app.register_blueprint(profesores_bp)

    # Login manager
    @login_manager.user_loader
    def load_user(id):
        padre = Padres.query.filter_by(padre_id=id).first()
        profesor = Profesor.query.filter_by(profesor_id=id).first()
        return padre or profesor

    # Cargar datos en la db

    # adrian = Alumnos(name_alumno='Adrian Mendoza', ci_alumno=5706998, grupo='5A')
    # maria = Alumnos(name_alumno='Maria Lopez', ci_alumno=5754398, grupo='5B')
    # ramiro= Alumnos(name_alumno='Ramiro Perez', ci_alumno=5304598, grupo='5A')
    # alba= Alumnos(name_alumno='Alba Marin', ci_alumno=5123908, grupo='5B')
    # pablo= Alumnos(name_alumno='Pablo Gonzalez', ci_alumno=5419853, grupo='5A')
    # ariana= Alumnos(name_alumno='Pedro Escobar', ci_alumno=5706999, grupo='5B')
    # jana = Alumnos(name_alumno='Jana Ferreira', ci_alumno=5777456, grupo='5A')
    # pedro = Alumnos(name_alumno='Pedro Villalba', ci_alumno=5706432, grupo='5B')
    # sol = Alumnos(name_alumno='Sol Acosta', ci_alumno=5899432, grupo='5A')
    # esteban = Alumnos(name_alumno='Esteban Martinez', ci_alumno=6896998, grupo='5B')
    # carlos = Alumnos(name_alumno='Carlos Ortiz', ci_alumno=6344876, grupo='5A')
    # mariana= Alumnos(name_alumno='Mariana Ramirez', ci_alumno=5998886, grupo='5B')
    # alex= Alumnos(name_alumno='Alex Colman', ci_alumno=5667899, grupo='5A')
    # luis = Alumnos(name_alumno='Luis Montez', ci_alumno=5543345, grupo='5B')
    # israel = Alumnos(name_alumno='Israel Gimenez', ci_alumno=5988798, grupo='5A')
    # horacio = Alumnos(name_alumno='Horacio da Silva', ci_alumno=6543298, grupo='5B')
    # angelica = Alumnos(name_alumno='Angelica Martinetti', ci_alumno=7897654, grupo='5A')
    # sofia = Alumnos(name_alumno='Sofia Toffoletti', ci_alumno=6788769, grupo='5B')
    # blas = Alumnos(name_alumno='Blas Evers', ci_alumno=6543998, grupo='5A')
    # sebastian = Alumnos(name_alumno='Sebastian Alonso', ci_alumno=5232328, grupo='5B')
    # helga= Alumnos(name_alumno='Helga Miers', ci_alumno=5566775, grupo='5A')
    # angeles = Alumnos(name_alumno='Angeles Segovia', ci_alumno=4567876, grupo='5B')
    # patricio = Alumnos(name_alumno='Patricio Estigarribia', ci_alumno=5997799, grupo='5A')

    # gladys = Profesor(name='Gladys Torres', rol='profesor', ci=4265567, grupo='5A', password='gladys')
    # romina = Profesor(name='Romina Vera', rol='profesor', ci=3777409, grupo='5B', password='romina')
    # roberto = Profesor(name='Roberto Duarte', rol='profesor', ci=4888999, grupo='5A', password='roberto')
    # martina = Profesor(name='Martina Dominguez', rol='profesor', ci=4864321, grupo='5B', password='martina')

    # aviso1 = Avisos(titulo='AVISO-INICIO DE CLASES', cuerpo='Señores Padres/Encargados/Tutores Presente: Nos dirijimos a ustedes como institucion a fin de informar que, desde el martes 1 de marzo del corriente, retornamos a clases presenciales nivel inicial y primaria. El horario de clases turno mañana para Nivel inicial y primaria sera de 7:30 am hasta las 12:00 pm. El horario de clases turno tarde para Nivel inicial y primaria sera de 13:30 pm hasta las 17:30 pm. ¡¡¡Bienvenidos queridos alumnnos a este nuevo año electivo!!! Atte: La direccion.')
    # aviso2 = Avisos(titulo='Estimados padres y/o Encargados', cuerpo='Considerando las condiciones climáticas actuales y el pronóstico para esta tarde y; preservando la salud e integridad de nuestros alumnos, las clases de educación física del 2do ciclo y los talleres deportivos de hoy jueves 24 de marzo están suspendidas. Agradeciendo su comprensión, los saludo muy atentamente. Prof. Lic. Roberto Duarte.')
    # aviso3 = Avisos(titulo='Apreciados Padres de Familia del 5to grado:', cuerpo='Tenemos el agrado de invitarlos a participar de la Reunión General para Padres el dia 25 de marzo a las 07:30 am puntualmente. Las profesoras compartirán con ustedes normativas, calendario de actividades y procedimientos a seguir con respecto al año escolar de sus hijos. Finalizada la reunión se procederá a la Elección de Padres Delegados. atte: La Coordinacion.')
    # aviso4 = Avisos(titulo='AVISO-Lista de utiles', cuerpo='Estimados padres y/o Encargados: informamos que el kit de utiles escolares proveidos por el MEC estaran disponibles desde mañana en la direccion de la instucion para su entrega correspondiente a nuestros alummnos. La gestion del medio pasaje tambien empezara desde el dia de mañana. Atte: La direccion.')


    # with app.app_context():
    #     db.create_all()
    #     db.session.add_all([adrian, maria, ramiro, alba, pablo, ariana, jana, pedro, sol, esteban, carlos, mariana, alex, luis, israel, horacio, angelica, sofia, blas, sebastian, helga, angeles, patricio])
        # db.session.add_all([aviso1, aviso2, aviso3, aviso4])
        # db.session.commit()


    return app