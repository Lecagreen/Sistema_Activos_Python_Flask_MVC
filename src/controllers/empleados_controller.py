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

    @app.route('/modificar_empleado')
    def modificar_empleado():
        return render_template('formulario_modificar_empleado.html')

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
                'division': empleado['division'],
                'nombres': empleado['nombres'],
                'apellidos': empleado['apellidos'],
                'correoElectronico': empleado['correoElectronico']
            })
        else:
            print(f"No se encontró el empleado con idEmpleado: {idEmpleado}")
            return jsonify({'error': 'Empleado no encontrado'}), 404