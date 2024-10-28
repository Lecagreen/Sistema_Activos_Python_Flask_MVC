from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.modelos import Modelos
from src.models.marcas import Marcas

class ModelosController(FlaskController):
    @app.route('/crear_modelo', methods=['POST','GET'])
    def crear_modelo():
        if request.method == 'POST':
            modelo = request.form.get('modelo')
            marca = request.form.get('marca')
            modelo = Modelos(modelo, marca)
            Modelos.agregar_modelo(modelo)
            return redirect(url_for('ver_modelos'))
        marcas = Marcas.obtener_marcas()
        return render_template('formulario_crear_modelo.html', titulo_pagina = 'Crear Modelos', marcas=marcas)

    @app.route('/modificar_modelo')
    def modificar_modelo():
        return render_template('formulario_modificar_modelo.html')

    @app.route('/ver_modelos')
    def ver_modelos():
        modelos = Modelos.obtener_modelos()
        return render_template('tabla_modelos.html', titulo_pagina = 'Ver Modelos', modelos=modelos)