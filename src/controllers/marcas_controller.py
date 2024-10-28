from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.marcas import Marcas

class MarcasController(FlaskController):
    @app.route('/crear_marca', methods=['POST','GET'])
    def crear_marca():
        if request.method == 'POST':
            marca = request.form.get('marca')
            marca = Marcas(marca)
            Marcas.agregar_marca(marca)
            return redirect(url_for('ver_marcas'))
        return render_template('formulario_crear_marca.html', titulo_pagina = 'Crear Marca')

    @app.route('/modificar_marca')
    def modificar_marca():
        return render_template('formulario_modificar_marca.html')

    @app.route('/ver_marcas')
    def ver_marcas():
        marcas = Marcas.obtener_marcas()
        return render_template('tabla_marcas.html', titulo_pagina = 'Ver Marcas', marcas=marcas)
