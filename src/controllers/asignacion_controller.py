from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.asignaciones import Asignaciones
from src.models.empleados import Empleados
from src.models.activos import Activos
import datetime

class AsignacionesController(FlaskController):    
    @app.route("/asignaciones")
    def asignaciones():
        asignaciones = Asignaciones.obtener_asignaciones()
        return render_template('tabla_asignaciones.html', titulo="Lista de Asignaciones", asignaciones=asignaciones)

    @app.route("/crear_asignacion", methods=['GET','POST'])
    def crear_asignacion():
        if request.method == 'POST':
            fecha = request.form.get('fecha')
            empleado = request.form.get('empleado')
            activo = request.form.get('activo')
            if not fecha:
                flash('La fecha es un campo obligatorio')   
            elif not empleado:
                flash('El empleado es un campo obligatorio')     
            elif not activo:
                flash('El usuario es un campo obligatorio')     
            else:          
                asignacion = Asignaciones(fecha,empleado,activo)
                Asignaciones.agregar_asignacion(asignacion)
                return redirect(url_for('asignaciones'))    
        fecha =  datetime.datetime.now().strftime('%Y-%m-%d')
        empleados = Empleados.obtener_empleados()
        activos = Activos.obtener_activos()
        return render_template('formulario_asignacion.html', titulo="Asignacion", fecha=fecha, empleados=empleados, activos=activos)