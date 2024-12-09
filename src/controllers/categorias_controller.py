from src.app import app
from flask import render_template, request, redirect, url_for, flash
from flask_controller import FlaskController
from src.models.categorias import Categorias

class CategoriasController(FlaskController):

    @app.route('/crear_categoria', methods=['POST','GET'])
    def crear_categoria():
        if request.method == 'POST':
            categoria = request.form.get('categoria')
            categoria = Categorias(categoria)
            try:
                Categorias.agregar_categoria(categoria)
                flash("¡Categoría creada exitosamente!")
                return redirect(url_for('ver_categorias'))
            except Exception as e:
                flash(f"Error al crear la categoría: {str(e)}")
                return redirect(url_for('crear_categoria'))
        return render_template('formulario_crear_categoria.html', titulo_pagina = 'Crear Categoria')

    @app.route('/editar_categoria/<int:idCategoria>', methods=['POST', 'GET'])
    def editar_categoria(idCategoria):
        categoria_actual = Categorias.obtener_categoria_por_id(idCategoria)
        if request.method == 'POST':
            nueva_categoria = request.form.get('categoria')
            try:
                categoria_actual.categoria = nueva_categoria
                Categorias.editar_categoria(categoria_actual)
                flash("¡Categoría modificada exitosamente!")
                return redirect(url_for('ver_categorias'))
            except Exception as e:
                flash(f"Error al modificar la categoría: {str(e)}")
                return redirect(url_for('editar_categoria', idCategoria=idCategoria))
        categorias = Categorias.obtener_categorias()
        return render_template('formulario_editar_categoria.html', titulo_pagina='Editar Categoria', categoria_actual=categoria_actual, categorias=categorias)

    @app.route('/ver_categorias')
    def ver_categorias():
        categorias = Categorias.obtener_categorias()
        return render_template('tabla_categorias.html', titulo_pagina = 'Ver Categorias', categorias=categorias)
    
    @app.route('/eliminar_categoria/<int:idCategoria>', methods=['POST', 'GET'])
    def eliminar_categoria(idCategoria):
        categoria_actual = Categorias.obtener_categoria_por_id(idCategoria)

        if request.method == 'POST':
            cambio_estado = request.form.get('categoria')
            try:
                categoria_actual.categoria = cambio_estado
                categoria = Categorias.eliminar_categoria(idCategoria)
                if categoria:
                    flash("¡Categoría No Vigente!")
                else:
                    flash("Error: Marca no encontrada.")
            except Exception as e:
                flash(f"Error al intentar marcar la categoria como No Vigente: {str(e)}")
            return redirect(url_for('ver_categorias'))
        categorias = Categorias.obtener_categorias()
        return render_template('formulario_eliminar_categoria.html', titulo_pagina='Eliminar Categoria', 
                               categoria_actual=categoria_actual, categorias=categorias)