from src.blueprints.profesores import bp
from flask import redirect, url_for, render_template
from flask_login import login_required, current_user


    
@bp.route('/')
@login_required
def bienvenido_profesor():
    if current_user.rol == 'profesor':
         return render_template('profesores/bienvenida.html')
    else:
        return redirect(url_for('padres.padres_home'))

# endopoint para el menu de profesores que recibe el curso en string
@bp.route('/profesores/<curso>')
def menu_profe(curso):
    # return "este es el curso: {0}".format(curso)
    return render_template('profesores/menu-profe.html')

@bp.route('/profesores/<curso>/crear-aviso')
def crear_aviso(curso):
    # return "este es el curso: {0}".format(curso)

    # recibir datos del form

    # insertar los datos a la bd, en la tabla avisos


    return render_template('profesores/crear-aviso.html')

@bp.route('/estudiantes-avisos')
def estudiantes_avisos():
    return render_template('profesores/estudiantes-avisos.html')

