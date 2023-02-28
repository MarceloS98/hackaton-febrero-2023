from flask import redirect, url_for
from src.blueprints.profesores import bp
from flask_login import login_required, current_user

@bp.route('/')
@login_required
def profes_home():
    print(current_user.name)
    if current_user.rol == 'profesor':
        return 'Pagina para Profesores'
    else:
        return redirect(url_for('padres.padres_home'))

