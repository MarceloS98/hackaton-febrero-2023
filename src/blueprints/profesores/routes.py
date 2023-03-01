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
   

@bp.route('/crear-aviso')
def crear_aviso():
    return render_template('profesores/crear-aviso.html')

@bp.route('/estudiantes-avisos')
def estudiantes_avisos():
    return render_template('profesores/estudiantes-avisos.html')

@bp.route('/menu-profe')
def menu_profe():
    return render_template('profesores/menu-profe.html')

@bp.route('/enviados-avisos')
def enviados_avisos():
    return render_template('profesores/enviados-avisos.html')

@bp.route('/estudiantes-avisos')
def seleccionar_estudiantes():
    return render_template('profesores/estudiantes-avisos.html')

@bp.route('/check-avisos')
def aviso_enviado():
    return render_template('profesores/check-avisos.html')

@bp.route('/libreta-profesor')
def libreta_profesor():
    return render_template('profesores/libreta-profesor.html')

@bp.route('/check-libreta')
def libreta_guardada():
    return render_template('profesores/check-libreta.html')

@bp.route('/plantilla-estudiantes')
def seleccionar_estudiantes2():
    return render_template('profesores/plantilla-estudiante.html')

