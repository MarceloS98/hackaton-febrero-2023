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