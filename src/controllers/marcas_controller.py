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

    @app.route('/editar_marca/<int:idMarca>', methods=['POST', 'GET'])
    def editar_marca(idMarca):
        marca_actual = Marcas.obtener_marca_por_id(idMarca)
        if request.method == 'POST':
            nueva_marca = request.form.get('marca')
            try:
                marca_actual.marca = nueva_marca
                Marcas.editar_marca(marca_actual)
                flash("¡Marca modificada exitosamente!")
                return redirect(url_for('ver_marcas'))
            except Exception as e:
                flash(f"Error al modificar el marca: {str(e)}")
                return redirect(url_for('editar_marca', idMarca=idMarca))
        marcas = Marcas.obtener_marcas()
        return render_template('formulario_editar_marca.html', titulo_pagina='Editar Marca', marca_actual=marca_actual, marcas=marcas)

    @app.route('/ver_marcas')
    def ver_marcas():
        marcas = Marcas.obtener_marcas()
        return render_template('tabla_marcas.html', titulo_pagina = 'Ver Marcas', marcas=marcas)
