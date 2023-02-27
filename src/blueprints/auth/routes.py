from src.blueprints.auth import bp
from flask import flash, request
from flask_login import login_user, current_user, login_required, logout_user
from src.models.padres import Padres
from src.models.profesor import Profesor
from flask import render_template, redirect, url_for

@bp.route('/')
def login():
    return render_template('auth/login.html')

@bp.route('/', methods=['POST'])
def login_validator():
    ci = request.form.get('ci')
    password = request.form.get('password')

    user_padre = Padres.query.filter_by(ci=ci).first()
    user_profe = Profesor.query.filter_by(ci=ci).first()
    
    user = user_padre or user_profe
    
    # Chequea si el usuario existe
    # toma el user-supplied password, hashea, y lo compara con la contrasenha hasheada en la base de datos
    if not user:
        flash('Please check your login details and try again.')
    
    elif password != user.password: 
        flash('Please check your login details and try again.')
    
        # return redirect(url_for('bp.login')) # if the user doesn't exist or password is wrong, reload the page
    else:
        if password == user.password and user.rol == 'padre':
            login_user(user)
            print(current_user)
            print('hola')
            return redirect(url_for('auth.padres_login'))
            

        elif password == user.password and user.rol == 'profesor':
            login_user(user)
            print(current_user)
            return redirect(url_for('auth.profe_login'))
        # if the above check passes, then we know the user has the right credentials

    
    
    return render_template('auth/login.html')

@bp.route('/profe')
@login_required
def profe_login():

        return 'Pagina para Profesores'

@bp.route('/padres')
@login_required
def padres_login():
    return 'Pagina para padres'



    

@bp.route('/logout')
@login_required                        #el usuario debe estar logeado para poder salir
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

