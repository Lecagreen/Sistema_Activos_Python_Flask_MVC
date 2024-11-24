from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.asignaciones import Asignaciones
from src.models.empleados import Empleados
from src.models.activos import Activos
from src.models.categorias import Categorias
from src.models.tipos import Tipos
from src.models.divisiones import Divisiones
import datetime

class AsignacionesController(FlaskController):    
    @app.route("/ver_asignaciones")
    def asignaciones():
        asignaciones = Asignaciones.obtener_asignaciones()
        return render_template('tabla_asignaciones.html', titulo="Lista de Asignaciones", asignaciones=asignaciones)

    @app.route("/crear_asignacion", methods=['GET','POST'])
    def crear_asignacion():
        if request.method == 'POST':
            fecha = request.form.get('fecha')
            empleado = request.form.get('idEmpleado')
            activo = request.form.get('idActivo')
            if not fecha:
                flash('La fecha es un campo obligatorio')   
            elif not empleado:
                flash('El empleado es un campo obligatorio')     
            elif not activo:
                flash('El activo es un campo obligatorio')     
            else:          
                asignacion = Asignaciones(fecha,empleado,activo)
                Asignaciones.agregar_asignacion(asignacion)
                return redirect(url_for('ver_asignaciones'))  
              
        fecha =  datetime.datetime.now().strftime('%Y-%m-%d')
        empleados = Empleados.obtener_empleados_asignacion()
        activos = Activos.obtener_activos_asignacion()
        return render_template('formulario_asignacion.html', titulo="Asignacion", fecha=fecha, empleados=empleados, activos=activos)
    
    @app.route('/editar_asignacion/<int:idAsignacion>', methods=['POST', 'GET'])
    def editar_asignacion(idAsignacion):
        asignacion_actual, empleado_info, activo_info = Asignaciones.obtener_asignacion_por_id(idAsignacion)

        if asignacion_actual is None:
            flash("Asignación no encontrada")
            return redirect(url_for('ver_asignaciones'))

        empleados = Empleados.obtener_empleados_asignacion()
        activos = Activos.obtener_activos_asignacion()
        categoria = Categorias.obtener_categoria_por_id(activo_info.categoria)
        tipo = Tipos.obtener_tipo_por_id(activo_info.tipo)
        division = Divisiones.obtener_division_por_id(activo_info.division)
        
        if request.method == 'POST':
            try:
                asignacion_actual.fecha = request.form.get('fecha')
                asignacion_actual.empleado = request.form.get('idEmpleado')
                asignacion_actual.activo = request.form.get('idActivo')

                Asignaciones.editar_asignacion(asignacion_actual)
                flash("¡Asignación modificada exitosamente")
                return redirect(url_for('ver_asignaciones'))
            except Exception as e:
                flash(f"Error al modificar la asignacion: {str(e)}")
                return redirect(url_for('editar_asignacion', idAsignacion=idAsignacion))
            
        return render_template('formulario_editar_asignacion.html', titulo_pagina='Editar Asignacion', 
                               asignacion_actual=asignacion_actual, empleados=empleados, activos=activos, 
                               activo_info=activo_info, empleado_info=empleado_info, categoria=categoria, tipo=tipo, division=division)

