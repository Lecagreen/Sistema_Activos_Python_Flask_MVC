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

    @app.route('/editar_modelo/<int:idModelo>', methods=['POST', 'GET'])
    def editar_modelo(idModelo):
        modelo_actual = Modelos.obtener_modelo_por_id(idModelo)
        marcas = Marcas.obtener_marcas()

        if not modelo_actual:
            flash("Modelo no encontrado")
            return redirect(url_for("ver_modelos"))

        if request.method == 'POST':
            try:
                modelo_actual.modelo = request.form.get('modelo')
                modelo_actual.marca = request.form.get('marca')

                Modelos.editar_modelo(modelo_actual)
                flash("¡Modelo modfificado exitosamente!")
                return redirect(url_for('ver_modelos'))
            except Exception as e:
                flash(f"Erros al modificar el modelo: {str(e)}")
                return redirect(url_for('editar_modelo', idModelo=idModelo))
        modelos = Modelos.obtener_modelos()     
        return render_template('formulario_editar_modelo.html', titulo_pagina = 'Ver Modelos', 
                               modelo_actual=modelo_actual, marcas=marcas)

    @app.route('/ver_modelos')
    def ver_modelos():
        modelos = Modelos.obtener_modelos()
        return render_template('tabla_modelos.html', titulo_pagina = 'Ver Modelos', modelos=modelos)