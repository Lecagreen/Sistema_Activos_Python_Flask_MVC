from src.app import app
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_controller import FlaskController
from src.models.empleados import Empleados
from src.models.divisiones import Divisiones

class EmpleadosController(FlaskController):
    @app.route('/crear_empleado', methods=['POST','GET'])
    def crear_empleado():
        if request.method == 'POST':
            usuarioAdv = request.form.get('usuarioAdv')
            division = request.form.get('division')
            nombres = request.form.get('nombres')
            apellidos = request.form.get('apellidos')
            correoElectronico = request.form.get('correoElectronico')
            empleado = Empleados(usuarioAdv,division,nombres,apellidos,correoElectronico)
            Empleados.agregar_empleado(empleado)
            return redirect(url_for('ver_empleados'))
        divisiones = Divisiones.obtener_divisiones()
        return render_template('formulario_crear_empleado.html', titulo_pagina = 'Crear Empleado', divisiones=divisiones)

    @app.route('/editar_empleado/<int:idEmpleado>', methods=['POST', 'GET'])
    def editar_empleado(idEmpleado):
        empleado_actual = Empleados.obtener_empleado_por_id(idEmpleado)
        divisiones = Divisiones.obtener_divisiones()
        
        if not empleado_actual:
            flash("Empleado no encontrado")
            return redirect(url_for('ver_empleados'))

        if request.method == 'POST':
            try:
                empleado_actual.usuarioAdv = request.form.get('usuarioAdv')
                empleado_actual.division = request.form.get('division')
                empleado_actual.nombres = request.form.get('nombres')
                empleado_actual.apellidos = request.form.get('apellidos')
                empleado_actual.correoElectronico = request.form.get('correoElectronico')

                Empleados.editar_empleado(empleado_actual)
                flash("¡Empleado modificado exitosamente!")
                return redirect(url_for('ver_empleados'))
            except Exception as e:
                flash(f"Error al modificar el empleado: {str(e)}")
                return redirect(url_for('editar_empleado', idEmpleado=idEmpleado))

        return render_template('formulario_editar_empleado.html', titulo_pagina='Editar Empleado',
                               empleado_actual=empleado_actual, divisiones=divisiones)

    @app.route('/ver_empleados')
    def ver_empleados():
        empleados = Empleados.obtener_empleados()
        return render_template('tabla_empleados.html', titulo_pagina = 'Ver Empleados', empleados=empleados)
    
    @app.route("/empleados/<idEmpleado>")
    def ver_empleado(idEmpleado):
        print(f"Buscando empleado con usuarioAdv: {idEmpleado}")
        empleado = Empleados.obtener_empleado_por_id(idEmpleado)
        if empleado:
            print(f"Empleado encontrado: {empleado}")
            return jsonify({
                'divisionEmpleado': empleado['divisionEmpleado'],
                'nombres': empleado['nombres'],
                'apellidos': empleado['apellidos'],
                'correoElectronico': empleado['correoElectronico']
            })
        else:
            print(f"No se encontró el empleado con idEmpleado: {idEmpleado}")
            return jsonify({'error': 'Empleado no encontrado'}), 404