from src.blueprints.padres import bp
from flask import redirect, url_for, render_template
from flask_login import login_required, current_user

@bp.route('/')
@login_required
def padres_home():
    print(current_user.name)
    if current_user.rol == 'padre':
        return render_template('padres/padres-menu.html')
    else:
        return redirect(url_for('profesores.profes_home'))
    
@bp.route('/padres-menu')
def padres_menu():
    return render_template('padres/padres-menu.html')

@bp.route('/padres-libreta')
def padres_libreta():
    return render_template('padres/padres-libreta.html')