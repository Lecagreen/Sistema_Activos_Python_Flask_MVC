from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.ubicaciones import Ubicaciones

class UbicacionesController(FlaskController):
    @app.route('/crear_ubicacion', methods=['POST','GET'])
    def crear_ubicacion():
        if request.method == 'POST':
            ubicacion = request.form.get('ubicacion')
            piso = request.form.get('piso')
            puesto = request.form.get('puesto')
            ubicacion = Ubicaciones(ubicacion,piso,puesto)
            Ubicaciones.agregar_ubicacion(ubicacion)
            return redirect(url_for('ver_ubicaciones'))
        return render_template('formulario_crear_ubicacion.html', titulo_pagina = 'Crear Ubicacion')

    @app.route('/modificar_ubicacion')
    def modificar_ubicacion():
        return render_template('formulario_modificar_ubicacion.html')

    @app.route('/ver_ubicaciones')
    def ver_ubicaciones():
        ubicaciones = Ubicaciones.obtener_ubicaciones()
        return render_template('tabla_ubicaciones.html', titulo_pagina = 'Ver Ubicaciones', ubicaciones=ubicaciones)