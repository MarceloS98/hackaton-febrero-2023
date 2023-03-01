from flask import request
from src.blueprints.profesores import bp
from flask import redirect, url_for, render_template, request
from flask_login import login_required, current_user
from src.models.avisos import Avisos
from src.utils.send_message import send_sms
from credentials import account_sid, auth_token


@bp.route('/')
@login_required
def bienvenido_profesor():
    if current_user.rol == 'profesor':
         return render_template('profesores/bienvenida.html', name=current_user.name, grupo=current_user.grupo)
    else:
        return redirect(url_for('padres.padres_home'))

@bp.route('/crear-aviso', methods=['GET', 'POST'])
@login_required
def crear_aviso():
    if current_user.rol == 'profesor':
        if request.method == 'POST':
            titulo = request.form['titulo']
            cuerpo = request.form['cuerpo']

            aviso = Avisos(titulo=titulo, cuerpo=cuerpo, profesor=current_user)

            print(aviso)

            return redirect(url_for('profesores.estudiantes_avisos'))

        return render_template('profesores/crear-aviso.html')    
    else:
        return redirect(url_for('padres.padres_home'))
        

@bp.route('/estudiantes-avisos', methods=['GET', 'POST'])
@login_required
def estudiantes_avisos():
    if current_user.rol == 'profesor':

        if request.method == 'POST':
            nro_padre_alumno = request.form.getlist('alumnos')
            
            send_sms( account_sid=account_sid, auth_token=auth_token ,to_number='+595972589778', body='Tu hijo falto encargados')

            return redirect(url_for('profesores.aviso_enviado'))

        return render_template('profesores/estudiantes-avisos.html', alumnos=current_user.alumnos)
    else:
        return redirect(url_for('padres.padres_home'))

@bp.route('/menu-profe')
@login_required
def menu_profe():
    if current_user.rol == 'profesor':
        return render_template('profesores/menu-profe.html')
    else:
        return redirect(url_for('padres.padres_home'))

@bp.route('/enviados-avisos')
@login_required
def enviados_avisos():
    print(current_user.avisos)
    if current_user.rol == 'profesor':
        return render_template('profesores/enviados-avisos.html')
    else:
        return redirect(url_for('padres.padres_home'))

@bp.route('/estudiantes-avisos')
@login_required
def seleccionar_estudiantes():
    if current_user.rol == 'profesor':
        return render_template('profesores/estudiantes-avisos.html')
    else:
        return redirect(url_for('padres.padres_home'))

@bp.route('/check-avisos')
@login_required
def aviso_enviado():
    if current_user.rol == 'profesor':
        return render_template('profesores/check-avisos.html')
    else:
        return redirect(url_for('padres.padres_home'))

@bp.route('/libreta-profesor')
@login_required
def libreta_profesor():
    if current_user.rol == 'profesor':
        return render_template('profesores/libreta-profesor.html')
    else:
        return redirect(url_for('padres.padres_home'))

@bp.route('/check-libreta')
@login_required
def libreta_guardada():
    if current_user.rol == 'profesor':
        return render_template('profesores/check-libreta.html')
    else:
        return redirect(url_for('padres.padres_home'))

@bp.route('/plantilla-estudiantes')
@login_required
def seleccionar_estudiantes2():
    if current_user.rol == 'profesor':
        return render_template('profesores/plantilla-estudiante.html')
    else:
        return redirect(url_for('padres.padres_home'))

