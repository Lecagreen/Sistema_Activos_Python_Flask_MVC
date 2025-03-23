from src.app import app
from flask import render_template, request, redirect, url_for, jsonify, flash
from flask_controller import FlaskController
from src.models.activos import Activos
from src.models.marcas import Marcas
from src.models.modelos import Modelos
from src.models.categorias import Categorias
from src.models.divisiones import Divisiones
from src.models.tipos import Tipos
from flask_restful import Api
from src.api.activos_api import ActivosApi


class ActivosController(FlaskController):

    api = Api(app)

    api.add_resource(ActivosApi, '/api/activos')
    
    @app.route('/crear_activo', methods=['POST', 'GET'])
    def crear_activo():
        if request.method == 'POST':
            codigo = request.form.get('codigo')
            categoria = request.form.get('categoria')
            tipo = request.form.get('tipo')
            caracteristicas = request.form.get('caracteristicas')
            marca = request.form.get('marca') or None
            modelo = request.form.get('modelo') or None
            serial = request.form.get('serial') or None
            largo = request.form.get('largo') or None
            ancho = request.form.get('ancho') or None
            alto = request.form.get('alto') or None
            diametro = request.form.get('diametro') or None
            division = request.form.get('division')

            if not all([codigo, tipo, categoria, caracteristicas, division]):
                raise ValueError("Los campos obligatorios no pueden contener valores nulos.")

            activo = Activos(codigo, categoria, tipo, caracteristicas, marca, modelo, serial, largo, ancho, alto, diametro, division)
            resultado = Activos.agregar_activo(activo)
            if resultado:
                print("Activo agregado exitosamente.")
            else:
                print("Hubo un problema al agregar el activo.")

            return redirect(url_for('ver_activos'))

        categorias = Categorias.obtener_categorias()
        tipos = Tipos.obtener_tipos_activo()
        divisiones = Divisiones.obtener_divisiones()
        marcas = Marcas.obtener_marcas()
        modelos = Modelos.obtener_modelos_activo()
        return render_template('formulario_crear_activo.html', titulo_pagina='Crear Activo', categorias=categorias, tipos=tipos, divisiones=divisiones, marcas=marcas, modelos=modelos)
    
    @app.route('/editar_activo/<int:idActivo>', methods=['POST', 'GET'])
    def editar_activo(idActivo):
        activo_actual = Activos.obtener_activo_por_id(idActivo)
        categorias = Categorias.obtener_categorias()
        tipos = Tipos.obtener_tipos_activo()
        marcas = Marcas.obtener_marcas()
        modelos = Modelos.obtener_modelos_activo()        
        divisiones = Divisiones.obtener_divisiones()
        
        if not activo_actual:
            flash("Activo no encontrado")
            return redirect(url_for('ver_activos'))

        if request.method == 'POST':
            try:
                activo_actual.codigo = request.form.get('codigo')
                activo_actual.categoria = request.form.get('categoria')
                activo_actual.tipo = request.form.get('tipo')
                activo_actual.caracteristicas = request.form.get('caracteristicas')
                activo_actual.marca = request.form.get('marca')
                activo_actual.modelo = request.form.get('modelo')
                activo_actual.serial = request.form.get('serial')
                activo_actual.largo = request.form.get('largo')
                activo_actual.ancho = request.form.get('ancho')
                activo_actual.alto = request.form.get('alto')
                activo_actual.diametro = request.form.get('diametro')
                activo_actual.division = request.form.get('division')

                Activos.editar_activo(activo_actual)
                flash("¡Activo modificado exitosamente!")
                return redirect(url_for('ver_activos'))
            except Exception as e:
                flash(f"Error al modificar el activo: {str(e)}")
                return redirect(url_for('editar_activo', idActivo=idActivo))

        return render_template('formulario_editar_activo.html', titulo_pagina='Editar Activo',
                               activo_actual=activo_actual, categorias=categorias, tipos=tipos, marcas=marcas, modelos=modelos, divisiones=divisiones)

    @app.route('/ver_activos')
    def ver_activos():
        activos = Activos.obtener_activos()
        if not activos:
            print("No se encontraron activos para mostrar.")
        return render_template('tabla_activos.html', titulo_pagina='Ver Activos', activos=activos)
    
    @app.route("/activos/<idActivo>")
    def ver_activo(idActivo):
        print(f"Buscando activo con codigo: {idActivo}")
        activo = Activos.obtener_activo_asignacion(idActivo)
        if activo:
            print(f"Activo encontrado: {activo}")
            return jsonify({
                'categoriaActivo': activo.get('categoriaActivo'),
                'tipoActivo': activo.get('tipoActivo'),
                'caracteristicas': activo.get('caracteristicas'),
                'divisionActivo': activo.get('divisionActivo')
            })
        else:
            print(f"No se encontró el activo con idActivo: {idActivo}")
            return jsonify({'error': 'Activo no encontrado'}), 404