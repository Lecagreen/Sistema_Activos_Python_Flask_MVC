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

    @app.route('/editar_ubicacion/<int:idUbicacion>', methods=['POST', 'GET'])
    def editar_ubicacion(idUbicacion):
        ubicacion_actual = Ubicaciones.obtener_ubicacion_por_id(idUbicacion)

        if not ubicacion_actual:
            flash("Ubicacion no encontrada")
            return redirect(url_for("ver_ubicaciones"))
        
        if request.method == 'POST':
            try:
                ubicacion_actual.ubicacion = request.form.get('ubicacion')
                ubicacion_actual.piso = request.form.get('piso')
                ubicacion_actual.puesto = request.form.get('puesto')

                Ubicaciones.editar_ubicacion(ubicacion_actual)
                flash("¡Ubicacion modificada exitosamente!")
                return redirect(url_for('ver_ubicaciones'))
            except Exception as e:
                flash(f"Error al modificar la ubicacion: {str(e)}")
                return redirect(url_for('editar_ubicacion', idUbicacion=idUbicacion))
        ubicaciones = Ubicaciones.obtener_ubicaciones()
        return render_template('formulario_editar_ubicacion.html', titulo_pagina='Editar Ubicacion',
                               ubicacion_actual=ubicacion_actual, ubicaciones=ubicaciones)

    @app.route('/ver_ubicaciones')
    def ver_ubicaciones():
        ubicaciones = Ubicaciones.obtener_ubicaciones()
        return render_template('tabla_ubicaciones.html', titulo_pagina = 'Ver Ubicaciones', ubicaciones=ubicaciones)