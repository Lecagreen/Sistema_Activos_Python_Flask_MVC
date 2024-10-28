from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.tipos import Tipos
from src.models.categorias import Categorias

class TiposController(FlaskController):
    @app.route('/crear_tipo', methods=['POST','GET'])
    def crear_tipo():
        if request.method == 'POST':
            tipo = request.form.get('tipo')
            categoria = request.form.get('categoria')
            tipo = Tipos(tipo, categoria)
            Tipos.agregar_tipo(tipo)
            return redirect(url_for('ver_tipos'))
        categorias = Categorias.obtener_categorias()
        return render_template('formulario_crear_tipo.html', titulo_pagina = 'Crear Tipo', categorias=categorias)

    @app.route('/modificar_tipo')
    def modificar_tipo():
        return render_template('formulario_modificar_tipo.html')

    @app.route('/ver_tipos')
    def ver_tipos():
        tipos = Tipos.obtener_tipos()
        return render_template('tabla_tipos.html', titulo_pagina = 'Ver Tipos', tipos=tipos)