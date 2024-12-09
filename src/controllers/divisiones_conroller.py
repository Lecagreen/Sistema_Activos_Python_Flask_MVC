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

    @app.route('/editar_division/<int:idDivision>', methods=['POST', 'GET'])
    def editar_division(idDivision):
        division_actual = Divisiones.obtener_division_por_id(idDivision)
        if request.method == 'POST':
            nueva_division = request.form.get('division')
            try:
                division_actual.division = nueva_division
                Divisiones.editar_division(division_actual)
                flash("¡Division modificado exitosamente!")
                return redirect(url_for('ver_divisiones'))
            except Exception as e:
                flash(f"Error al modificar la division: {str(e)}")
                return redirect(url_for('editar_division', idDivision=idDivision))
        divisiones = Divisiones.obtener_divisiones()
        return render_template('formulario_editar_division.html', titulo_pagina='Editar Division', division_actual=division_actual, divisiones=divisiones)

    @app.route('/ver_divisiones')
    def ver_divisiones():
        divisiones = Divisiones.obtener_divisiones()
        return render_template('tabla_divisiones.html', titulo_pagina = 'Ver Divisiones', divisiones=divisiones)
    
    @app.route('/eliminar_division/<int:idDivision>', methods=['POST', 'GET'])
    def eliminar_division(idDivision):
        division_actual = Divisiones.obtener_division_por_id(idDivision)
        if not division_actual:
            flash("Division no encontrado")
            return redirect(url_for('ver_divisiones'))
        if request.method == 'POST':
            try:
                division_actual.estado = 'NO'
                Divisiones.editar_division(division_actual)  
                flash("¡Division marcado como no vigente!")
            except Exception as e:
                flash(f"Error al eliminar el division: {str(e)}")
            return redirect(url_for('ver_divisiones'))
        divisiones = Divisiones.obtener_divisiones()
        return render_template('formulario_eliminar_division.html', titulo_pagina='Eliminar Division', 
                               division_actual=division_actual, divisiones=divisiones)