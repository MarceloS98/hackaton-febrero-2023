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
    
    # El user puede ser un padre o un profesor
    user = user_padre or user_profe    

    # Chequea si el usuario existe
    if not user:
        flash('Please check your login details and try again.')
    # Si la contraseña es incorrecta
    elif password != user.password: 
        flash('Please check your login details and try again.')
    # Si el usuario existe y la contraseña es correcta
    else:
        # Si el usuario es un padre
        if password == user.password and user.rol == 'padre':
            login_user(user)
            print('Este es el current user', current_user)
            return redirect(url_for('padres.padres_home'))
        # Si el usuario es un profesor
        elif password == user.password and user.rol == 'profesor':
            login_user(user)
            print('Este es el current user', current_user)
            return redirect(url_for('profesores.profes_home'))

# Ruta para salir de la sesion
@bp.route('/logout')
@login_required #el usuario debe estar logeado para poder salir
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
