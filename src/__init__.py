import random
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

    # # Cargar datos en la db
    # # Padres
    # padre_1 = Padres(name='Juan Perez', nro_contacto=+595981237436, rol='padre', ci=1234567, password='juan')
    # padre_2 = Padres(name='Diego Lopez', nro_contacto=+595981237466, rol='padre', ci=2345678, password='diego')
    # padre_3 = Padres(name='Jorge Martinez', nro_contacto=+595971777409, rol='padre', ci=3456789, password='jorge')
    # padre_4 = Padres(name='Marta Ramirez',nro_contacto=+595981283273, rol='padre', ci=4567890, password='marta')
    # padre_5 = Padres(name='Julia Acosta', nro_contacto=+595983678905, rol='padre', ci=5678901, password='julia')
    # padre_6 = Padres(name='Matias Ortiz', nro_contacto=+595981786965, rol='padre', ci=6789012, password='matias') 
    # padre_7 = Padres(name='Morticia Gomez', nro_contacto=+595981654324, rol='padre', ci=7890123, password='morticia')
    # padre_8 = Padres(name='Mabel Fernandez', nro_contacto=+595981234643, rol='padre', ci=8901234, password='mabel')
    # padre_9 = Padres(name='Ana Rodriguez', nro_contacto=+595982567892, rol='madre', ci=4567891, password='ana')
    # padre_10 = Padres(name='Luis García', nro_contacto=+595982357949,  rol='padre', ci=5678912, password='luis')
    # padre_11 = Padres(name='Maria Garcia', nro_contacto=+595982357948, rol='madre', ci=2345678, password='maria')
    # padre_12 = Padres(name='Pedro Rodriguez', nro_contacto=+595972857395, rol='padre', ci=3456789, password='pedro')
    # padre_13 = Padres(name='Luisa Martinez', nro_contacto=+595992384376, rol='madre', ci=4567890, password='luisa')
    # padre_14 = Padres(name='Jose Ramirez', nro_contacto=+595998765456, rol='padre', ci=5678901, password='jose')
    # padre_15 = Padres(name='Ana Chavez', nro_contacto=+595997678999, rol='madre', ci=6789012, password='ana')
    # padre_16 = Padres(name='Carlos Fernandez', nro_contacto=+595971283374, rol='padre', ci=7890123, password='carlos')
    # padre_17 = Padres(name='Laura Torres', nro_contacto=+595993857485, rol='madre', ci=8901234, password='laura')
    # padre_18 = Padres(name='Manuel Garcia', nro_contacto=+595992583748, rol='padre', ci=9012345, password='manuel')
    # padre_19 = Padres(name='Liliana Gonzalez', nro_contacto=+595992384932, rol='madre', ci=1234567, password='liliana')
    # padre_20 = Padres(name='Antonio Perez', nro_contacto=+595983499588, rol='padre', ci=2345678, password='antonio')
    # padre_21 = Padres(name='Adriana Jimenez', nro_contacto=+595984736454, rol='madre', ci=3456789, password='adriana')
    # padre_22 = Padres(name='Juan Carlos Ortiz', nro_contacto=+595973495485, rol='padre', ci=4567890, password='juancarlos')

    # # Alumnos
    # alumno_1 = Alumnos(name_alumno='Adrian Mendoza', ci_alumno=5706998, grupo='5A')
    # alumno_2 = Alumnos(name_alumno='Maria Lopez', ci_alumno=5754398, grupo='5B')
    # alumno_3 = Alumnos(name_alumno='Ramiro Perez', ci_alumno=5304598, grupo='5A')
    # alumno_4 = Alumnos(name_alumno='Alba Marin', ci_alumno=5123908, grupo='5B')
    # alumno_5 = Alumnos(name_alumno='Pablo Gonzalez', ci_alumno=5419853, grupo='5A')
    # alumno_6 = Alumnos(name_alumno='Pedro Escobar', ci_alumno=5706999, grupo='5B')
    # alumno_7 = Alumnos(name_alumno='Jana Ferreira', ci_alumno=5777456, grupo='5A')
    # alumno_8 = Alumnos(name_alumno='Pedro Villalba', ci_alumno=5706432, grupo='5B')
    # alumno_9 = Alumnos(name_alumno='Sol Acosta', ci_alumno=5899432, grupo='5A')
    # alumno_10 = Alumnos(name_alumno='Esteban Martinez', ci_alumno=6896998, grupo='5B')
    # alumno_11 = Alumnos(name_alumno='Carlos Ortiz', ci_alumno=6344876, grupo='5A')
    # alumno_12 = Alumnos(name_alumno='Mariana Ramirez', ci_alumno=5998886, grupo='5B')
    # alumno_13 = Alumnos(name_alumno='Alex Colman', ci_alumno=5667899, grupo='5A')
    # alumno_14 = Alumnos(name_alumno='Luis Montez', ci_alumno=5543345, grupo='5B')
    # alumno_15 = Alumnos(name_alumno='Israel Gimenez', ci_alumno=5988798, grupo='5A')
    # alumno_16 = Alumnos(name_alumno='Horacio da Silva', ci_alumno=6543298, grupo='5B')
    # alumno_17 = Alumnos(name_alumno='Angelica Martinetti', ci_alumno=7897654, grupo='5A')
    # alumno_18 = Alumnos(name_alumno='Sofia Toffoletti', ci_alumno=6788769, grupo='5B')
    # alumno_19 = Alumnos(name_alumno='Blas Evers', ci_alumno=6543998, grupo='5A')
    # alumno_20 = Alumnos(name_alumno='Sebastian Alonso', ci_alumno=5232328, grupo='5B')
    # alumno_21 = Alumnos(name_alumno='Helga Miers', ci_alumno=5566775, grupo='5A')
    # alumno_22 = Alumnos(name_alumno='Angeles Segovia', ci_alumno=4567876, grupo='5B')

    # # Profesores
    # profesora = Profesor(name='Gladys Torres', rol='profesor', ci=4265567, grupo='5A', password='gladys')

    # # Avisos
    # aviso1 = Avisos(titulo='AVISO-INICIO DE CLASES', cuerpo='Señores Padres/Encargados/Tutores Presente: Nos dirijimos a ustedes como institucion a fin de informar que, desde el martes 1 de marzo del corriente, retornamos a clases presenciales nivel inicial y primaria. El horario de clases turno mañana para Nivel inicial y primaria sera de 7:30 am hasta las 12:00 pm. El horario de clases turno tarde para Nivel inicial y primaria sera de 13:30 pm hasta las 17:30 pm. ¡¡¡Bienvenidos queridos alumnnos a este nuevo año electivo!!! Atte: La direccion.')
    # aviso2 = Avisos(titulo='Estimados padres y/o Encargados', cuerpo='Considerando las condiciones climáticas actuales y el pronóstico para esta tarde y; preservando la salud e integridad de nuestros alumnos, las clases de educación física del 2do ciclo y los talleres deportivos de hoy jueves 24 de marzo están suspendidas. Agradeciendo su comprensión, los saludo muy atentamente. Prof. Lic. Roberto Duarte.')
    # aviso3 = Avisos(titulo='Apreciados Padres de Familia del 5to grado:', cuerpo='Tenemos el agrado de invitarlos a participar de la Reunión General para Padres el dia 25 de marzo a las 07:30 am puntualmente. Las profesoras compartirán con ustedes normativas, calendario de actividades y procedimientos a seguir con respecto al año escolar de sus hijos. Finalizada la reunión se procederá a la Elección de Padres Delegados. atte: La Coordinacion.')
    # aviso4 = Avisos(titulo='AVISO-Lista de utiles', cuerpo='Estimados padres y/o Encargados: informamos que el kit de utiles escolares proveidos por el MEC estaran disponibles desde mañana en la direccion de la instucion para su entrega correspondiente a nuestros alummnos. La gestion del medio pasaje tambien empezara desde el dia de mañana. Atte: La direccion.')        

    # # Materias
    # matematica = Materias(name='Matematica', etapa_1=random.randint(1, 5), etapa_2=random.randint(1, 5))
    # ciencias = Materias(name='Ciencias', etapa_1=random.randint(1, 5), etapa_2=random.randint(1, 5))
    # historia = Materias(name='Historia', etapa_1=random.randint(1, 5), etapa_2=random.randint(1, 5))
    # geografia = Materias(name='Geografia', etapa_1=random.randint(1, 5), etapa_2=random.randint(1, 5))
    # ingles = Materias(name='Ingles', etapa_1=random.randint(1, 5), etapa_2=random.randint(1, 5))
    # educacion_fisica = Materias(name='Educacion Fisica', etapa_1=random.randint(1, 5), etapa_2=random.randint(1, 5))
    # educacion_artistica = Materias(name='Educacion Artistica', etapa_1=random.randint(1, 5), etapa_2=random.randint(1, 5))
    # educacion_religiosa = Materias(name='Educacion Religiosa', etapa_1=random.randint(1, 5), etapa_2=random.randint(1, 5))
    
    # # Lista de materias
    # materias = [matematica, ciencias, historia, geografia, ingles, educacion_fisica, educacion_artistica, educacion_religiosa]
    # # Lista de padres
    # padres = [padre_1, padre_2, padre_3, padre_4, padre_5, padre_6, padre_7, padre_8, padre_9, padre_10, padre_11, padre_12, padre_13, padre_14, padre_15, padre_16, padre_17, padre_18, padre_19, padre_20, padre_21, padre_22]
    # # Lista de alumnos
    # alumnos = [alumno_1, alumno_2, alumno_3, alumno_4, alumno_5, alumno_6, alumno_7, alumno_8, alumno_9, alumno_10, alumno_11, alumno_12, alumno_13, alumno_14, alumno_15, alumno_16, alumno_17, alumno_18, alumno_19, alumno_20, alumno_21, alumno_22]
    # # Lista de avisos
    # avisos = [aviso1, aviso2, aviso3, aviso4]
    
    # # Avisos para tirar avisos random a los alumnos
    # lista_avisos = [ avisos, [aviso1, aviso2], [aviso3, aviso4], [aviso1], [aviso2], [aviso3], [aviso4] ]

    # with app.app_context():

    #     # Relaciones del alumno
    #     for alumno in alumnos: 
    #     # Many to many alumnos y avisos
    #         alumno.avisos = lista_avisos[random.randint(0, len(lista_avisos) - 1)]
    #     # Many to many alumnos y materias
    #         alumno.materias = materias

    #     # Relaciones del profesor
    #     # El profesor va a llevar todas las materias
    #     profesora.materias = materias
    #     # El profesor va a llevar todos los avisos
    #     profesora.avisos = avisos
    #     # El profesor va a tener todos los alumnos
    #     profesora.alumnos = alumnos

    #     # Relaciones del padre
    #     # Create one to one relationship between parents and students
    #     for i in range(len(padres)):
    #         padres[i].hijo = alumnos[i]

    #     db.create_all()
    #     db.session.add_all(alumnos)
    #     db.session.add_all(avisos)
    #     db.session.add_all(padres)
    #     db.session.commit()


    return app