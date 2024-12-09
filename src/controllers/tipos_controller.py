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

    @app.route('/editar_tipo/<int:idTipo>', methods=['POST', 'GET'])
    def editar_tipo(idTipo):
        tipo_actual = Tipos.obtener_tipo_por_id(idTipo)
        categorias = Categorias.obtener_categorias()

        if not tipo_actual:
            flash("Tipo no encontrado")
            return redirect(url_for("ver_tipos"))

        if request.method == 'POST':
            try:
                tipo_actual.tipo = request.form.get('tipo')
                tipo_actual.categoria = request.form.get('categoria')
                
                Tipos.editar_tipo(tipo_actual)
                flash("¡Tipo modificado exitosamente!")
                return redirect(url_for('ver_tipos'))
            except Exception as e:
                flash(f"Error al modificar el tipo: {str(e)}")
                return redirect(url_for('editar_tipo', idTipo=idTipo))
        
        return render_template('formulario_editar_tipo.html', titulo_pagina='Editar Tipo', 
                               tipo_actual=tipo_actual, categorias=categorias)

    @app.route('/ver_tipos')
    def ver_tipos():
        tipos = Tipos.obtener_tipos()
        return render_template('tabla_tipos.html', titulo_pagina = 'Ver Tipos', tipos=tipos)
    
    @app.route('/eliminar_tipo/<int:idTipo>', methods=['POST', 'GET'])
    def eliminar_tipo(idTipo):
        tipo_actual = Tipos.obtener_tipo_por_id(idTipo)
        if not tipo_actual:
            flash("Tipo no encontrado")
            return redirect(url_for('ver_tipos'))

        if request.method == 'POST':
            try:
                tipo_actual.estado = 'NO'
                Tipos.editar_tipo(tipo_actual)  

                flash("¡Tipo marcado como no vigente!")
            except Exception as e:
                flash(f"Error al eliminar el tipo: {str(e)}")
            return redirect(url_for('ver_tipos'))

        categorias = Categorias.obtener_categorias()
        return render_template('formulario_eliminar_tipo.html', titulo_pagina='Eliminar Tipo', 
                               tipo_actual=tipo_actual, categorias=categorias)