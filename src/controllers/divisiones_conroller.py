from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.divisiones import Divisiones

class DivisionesController(FlaskController):
    @app.route('/crear_division', methods=['POST','GET'])
    def crear_division():
        if request.method == 'POST':
            division = request.form.get('division')
            division = Divisiones(division)
            Divisiones.agregar_division(division)
            return redirect(url_for('ver_divisiones'))
        return render_template('formulario_crear_division.html', titulo_pagina = 'Crear Division')

    @app.route('/modificar_division')
    def modificar_division():
        return render_template('formulario_modificar_division.html')

    @app.route('/ver_divisiones')
    def ver_divisiones():
        divisiones = Divisiones.obtener_divisiones()
        return render_template('tabla_divisiones.html', titulo_pagina = 'Ver Divisiones', divisiones=divisiones)