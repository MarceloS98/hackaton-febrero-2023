from src.blueprints.padres import bp
from flask import redirect, url_for, render_template
from flask_login import login_required, current_user

@bp.route('/')
@login_required
def padres_menu():
    if current_user.rol == 'padre':
        return render_template('padres/padres-menu.html', padre=current_user) 
    else:
        return redirect(url_for('profesores.bienvenido_profesor'))


@bp.route('/padres-libreta')
@login_required
def padres_libreta():
    if current_user.rol == 'padre':    
        return render_template('padres/padres-libreta.html', materias=current_user.hijo.materias, hijo=current_user.hijo.name_alumno)
    else:
        return redirect(url_for('profesores.bienvenido_profesor'))

@bp.route('/padres-avisos')
@login_required
def padres_avisos():
    if current_user.rol == 'padre':
        return render_template('padres/recibidos-avisos.html')
    else:
        return redirect(url_for('profesores.bienvenido_profesor'))

