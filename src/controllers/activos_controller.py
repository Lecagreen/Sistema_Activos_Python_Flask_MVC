from src.app import app
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.models.activos import Activos
from src.models.marcas import Marcas
from src.models.modelos import Modelos
from src.models.categorias import Categorias
from src.models.divisiones import Divisiones
from src.models.tipos import Tipos

class ActivosController(FlaskController):

    @app.route('/crear_activo', methods=['POST', 'GET'])
    def crear_activo():
        if request.method == 'POST':
            codigo = request.form.get('codigo')
            categoria = request.form.get('categoria')
            tipo = request.form.get('tipo')
            division = request.form.get('division')
            caracteristicas = request.form.get('caracteristicas')
            marca = request.form.get('marca')
            modelo = request.form.get('modelo')
            serial = request.form.get('serial')
            largo = request.form.get('largo')
            ancho = request.form.get('ancho')
            alto = request.form.get('alto')
            diametro = request.form.get('diametro')

            print(f"codigo: {codigo}, tipo: {tipo}, categoria: {categoria}, caracteristicas: {caracteristicas}, division: {division}")

            if not all([codigo, tipo, categoria, caracteristicas, division]):
                raise ValueError("Los campos obligatorios no pueden contener valores nulos.")

            activo = Activos(codigo, tipo, categoria, caracteristicas, marca, modelo, serial, largo, ancho, alto, diametro, division)
            Activos.agregar_activo(activo)
            return redirect(url_for('ver_activos'))

        categorias = Categorias.obtener_categorias()
        tipos = Tipos.obtener_tipos()
        divisiones = Divisiones.obtener_divisiones()
        marcas = Marcas.obtener_marcas()
        modelos = Modelos.obtener_modelos()

        return render_template('formulario_crear_activo.html', titulo_pagina='Crear Activo', categorias=categorias, tipos=tipos, divisiones=divisiones, marcas=marcas, modelos=modelos)

    @app.route('/modificar_activo')
    def modificar_activo():
        return render_template('formulario_modificar_activo.html')

    @app.route('/ver_activos')
    def ver_activos():
        activos = Activos.obtener_activos()
        return render_template('tabla_activos.html', titulo_pagina = 'Ver Activos', activos=activos)