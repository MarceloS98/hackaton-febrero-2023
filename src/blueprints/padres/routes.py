from flask import redirect, url_for
from src.blueprints.padres import bp
from flask_login import login_required, current_user

@bp.route('/')
@login_required
def padres_home():
    print(current_user.name)
    if current_user.rol == 'padre':
        return 'Pagina para padres'
    else:
        return redirect(url_for('profesores.profes_home'))